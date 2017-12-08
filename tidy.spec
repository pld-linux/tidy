Summary:	Utility to clean up and pretty print HTML files
Summary(pl.UTF-8):	Narzędzie do porządkowania kodu HTML
Name:		tidy
Version:	5.6.0
Release:	1
Epoch:		1
License:	distributable
Group:		Applications/Text
#Source0Download: https://github.com/htacg/tidy-html5/releases
Source0:	https://github.com/htacg/tidy-html5/archive/5.6.0/tidy-html5-%{version}.tar.gz
# Source0-md5:	85c8a163d9ece6a02fe12bc9bddbc455
URL:		http://www.html-tidy.org/
BuildRequires:	cmake >= 2.8.12
BuildRequires:	libxslt-progs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tidy is utility for cleaning and pretty printing HTML files. It can
help in keeping your WWW sources in unified format (case of tags) and
proper encoding of different character sets.

%description -l pl.UTF-8
Tidy jest narzędziem służącym do czytelnego formatowania i
wyświetlania źródłowego kodu HTML. Ułatwia utrzymanie porządku w
źródłach stron WWW, utrzymanie jednolitej konwencji (wielkość liter w
tagach) oraz poprawnego kodowania różnych standardów znaków.

%package devel
Summary:	Tidy header files
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki dla programu Tidy
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Tidy header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki dla programu Tidy.

%package static
Summary:	Static Tidy library
Summary(pl.UTF-8):	Statyczna biblioteka Tidy
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static Tidy library.

%description static -l pl.UTF-8
Statyczna biblioteka Tidy.

%prep
%setup -q -n tidy-html5-%{version}

%build
install -d build
cd build
# .pc file template expects relative {INCLUDE,LIB}_INSTALL_DIR
%cmake .. \
	-DBUILD_TAB2SPACE=ON \
	-DINCLUDE_INSTALL_DIR=include/tidy \
	-DLIB_INSTALL_DIR=%{_lib} \
	-DTIDY_COMPAT_HEADERS=ON \
	-DTIDY_CONSOLE_SHARED=ON

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

# not installed
install build/tab2space $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md README/{API_AND_NAMESPACE.md,ATTRIBUTES.md,LICENSE.md,MESSAGES.md,OPTIONS.md,TAGS.md}
%attr(755,root,root) %{_bindir}/tab2space
%attr(755,root,root) %{_bindir}/tidy
%attr(755,root,root) %{_libdir}/libtidy.so.%{version}
%attr(755,root,root) %ghost %{_libdir}/libtidy.so.5
%{_mandir}/man1/tidy.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtidy.so
%{_includedir}/tidy
%{_pkgconfigdir}/tidy.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libtidys.a

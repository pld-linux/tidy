Summary:	Utility to clean up and pretty print HTML files
Summary(pl):	Narz�dzie do porz�dkowania kodu HTML
Name:		tidy
Version:	0.20050826
Release:	1
Epoch:		1
License:	distributable
Group:		Applications/Text
Source0:	http://tidy.sourceforge.net/src/tidy_src.tgz
# Source0-md5:	7c2ee7186b0384f92f65ec61266e0661
Source1:	http://tidy.sourceforge.net/docs/tidy_docs.tgz
# Source1-md5:	2e6533fc48b077ff6243deaf21a781de
URL:		http://tidy.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tidy is utility for cleaning and pretty printing HTML files. It can
help in keeping your WWW sources in unified format (case of tags) and
proper encoding of different character sets.

%description -l pl
Tidy jest narz�dziem s�u��cym do czytelnego formatowania i
wy�wietlania �r�d�owego kodu HTML. U�atwia utrzymanie porz�dku w
�r�d�ach stron WWW, utrzymanie jednolitej konwencji (wielko�� liter w
tagach) oraz poprawnego kodowania r�nych standard�w znak�w.

%package devel
Summary:	Tidy header files
Summary(pl):	Pliki nag��wkowe biblioteki dla programu Tidy
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Tidy header files.

%description devel -l pl
Pliki nag��wkowe biblioteki dla programu Tidy.

%package static
Summary:	Static Tidy library
Summary(pl):	Statyczna biblioteka Tidy
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static Tidy library.

%description static -l pl
Statyczna biblioteka Tidy.

%prep
%setup -q -n %{name} -b1

%build
cp -af build/gnuauto/* .
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc htmldoc/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%define		_snap	20061110
Summary:	Utility to clean up and pretty print HTML files
Summary(pl.UTF-8):   Narzędzie do porządkowania kodu HTML
Name:		tidy
Version:	0.%{_snap}
Release:	0.1
Epoch:		1
License:	distributable
Group:		Applications/Text
#Source0:	http://tidy.sourceforge.net/src/tidy_src.tgz
Source0:	%{name}-%{_snap}.tar.bz2
# Source0-md5:	872c0541d7693ff8a9c0961d67c5e871
Source1:	http://tidy.sourceforge.net/docs/%{name}_docs.tgz
# Source1-md5:	86de2f198e57399c063d2567b2a25628
URL:		http://tidy.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
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
Summary(pl.UTF-8):   Pliki nagłówkowe biblioteki dla programu Tidy
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Tidy header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki dla programu Tidy.

%package static
Summary:	Static Tidy library
Summary(pl.UTF-8):   Statyczna biblioteka Tidy
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static Tidy library.

%description static -l pl.UTF-8
Statyczna biblioteka Tidy.

%prep
%setup -q -c -b1
cd %{name}

%build
cd %{name}
cp -af build/gnuauto/* .
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
cd %{name}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc tidy/htmldoc/*
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

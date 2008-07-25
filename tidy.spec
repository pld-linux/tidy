%define		_snap	20080116
Summary:	Utility to clean up and pretty print HTML files
Summary(pl.UTF-8):	Narzędzie do porządkowania kodu HTML
Name:		tidy
Version:	0.%{_snap}
Release:	1
Epoch:		1
License:	distributable
Group:		Applications/Text
#Source0:	http://tidy.sourceforge.net/src/tidy_src.tgz
# tidy projects no longer releases tarballs. Use debian ones
Source0:	http://ftp.de.debian.org/debian/pool/main/t/tidy/tidy_20080116cvs.orig.tar.gz
# Source0-md5:	ff4558a920cfd7247f17e79b143f5a69
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
%setup -q -n %{name}-%{_snap}cvs

%build
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
%attr(755,root,root) %{_bindir}/tab2space
%attr(755,root,root) %{_bindir}/tidy
%attr(755,root,root) %{_libdir}/libtidy-0.99.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtidy-0.99.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtidy.so
%{_libdir}/libtidy.la
%{_includedir}/buffio.h
%{_includedir}/platform.h
%{_includedir}/tidy*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libtidy.a

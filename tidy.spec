%define		_snap	20091119
Summary:	Utility to clean up and pretty print HTML files
Summary(pl.UTF-8):	Narzędzie do porządkowania kodu HTML
Name:		tidy
Version:	0.%{_snap}
Release:	1
Epoch:		1
License:	distributable
Group:		Applications/Text
# tidy projects no longer releases tarballs.
# cvs -z3 -d:pserver:anonymous@tidy.cvs.sourceforge.net:/cvsroot/tidy export -D 2009-11-19 tidy
# tar -cf tidy-20091119.tar tidy;xz -9 -e tidy-20091119.tar
Source0:	tidy-%{_snap}.tar.xz
# Source0-md5:	0ca49cf79b4f3d25a080234a0bbf8eee
URL:		http://tidy.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
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
%setup -q -n %{name}

%build
sh build/gnuauto/setup.sh
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

Summary:	Utility to clean up and pretty print HTML files
Summary(pl):	Narzêdzie do porz±dkowania kodu HTML
Name:		tidy
Version:	0.20030702
Release:	1
License:	distributable
Group:		Applications/Text
Source0:        http://tidy.sf.net/src/tidy_src.tgz
# Source0-md5:	09e048c9aec1b72bc05bef97d1d28a89
Source1:	http://tidy.sf.net/docs/tidy_docs.tgz
# Source1-md5:	54ab968e177bc92495fce324c18f8b52
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
URL:	        http://tidy.sf.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tidy is utility for cleaning and pretty printing HTML files. It can
help in keeping your WWW sources in unified format (case of tags) and
proper encoding of different character sets.

%description -l pl
Tidy jest narzêdziem s³u¿±cym do czytelnego formatowania i
wy¶wietlania ¼ród³owego kodu HTML. U³atwia utrzymanie porz±dku w
¼ród³ach stron WWW, utrzymanie jednolitej konwecji (wielko¶æ liter w
tagach) oraz poprawnego kodowania ró¿nych standardów znaków.

%package devel
Summary:        Tidy header & static library files.
Summary(pl):    Pliki nag³ówkowe i biblioteki dla programu Tidy.
Group:          Developement

%description devel
Tidy header & static library files

%description -l pl devel
Pliki nag³ówkowe i biblioteki dla programu Tidy.

%prep
%setup -q -n %{name}
%setup -q -b1 -n %{name}

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

%files
%defattr(644,root,root,755)
%doc htmldoc/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*.h
%{_libdir}/*.a
%{_libdir}/*.la
%attr(755,root,root) %{_libdir}/*.so

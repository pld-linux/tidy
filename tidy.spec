# $Revision: 1.19 $ $Date: 2003-01-14 18:51:10 $
# TODO:
#   - Add docs from http://tidy.sourceforge.net/docs/tidy_docs.tgz
#   - Make all ac/am stuff. (Now only oryginal make is used)

Summary:	Utility to clean up and pretty print HTML files
Summary(pl):	Narzêdzie do porz±dkowania kodu HTML
Name:		tidy
Version:	20030101
Release:	0.9
License:	distributable
Group:		Applications/Text
Source0:        http://tidy.sourceforge.net/src/tidy_src.tgz
URL:	        http://tidy.sourceforge.net/
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

%build
#%%{__make} CFLAGS="%{rpmcflags}"
%{__make}


%install
rm -rf $RPM_BUILD_ROOT
# %%{__make} install \
#            DESTDIR=$RPM_BUILD_ROOT
# Above doesn't work so:

install -d $RPM_BUILD_ROOT{%{_bindir},%{_includedir}/%{name},%{_libdir}}
install bin/* ${RPM_BUILD_ROOT}%{_bindir}
install include/* ${RPM_BUILD_ROOT}%{_includedir}/%{name} 
install lib/* ${RPM_BUILD_ROOT}%{_libdir}

#install tidy ${RPM_BUILD_ROOT}%{_bindir}
#install tidy.1 ${RPM_BUILD_ROOT}%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%%doc Overview.html release-notes.html grid.gif tidy.gif
#%%{_mandir}/man1/*
%%attr(755,root,root) %{_bindir}/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}/*.h
%{_libdir}/*.a

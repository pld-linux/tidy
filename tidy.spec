# $Revision: 1.11 $ $Date: 2000-11-29 16:54:42 $
Summary:	Utility to clean up and pretty print HTML files
Summary(pl):	Narzêdzie do porz±dkowania kodu HTML
Name:		tidy
Version:	4aug00
Release:	1
Epoch:		1
Group:		Utilities/Text
Group(pl):	Narzêdzia/Tekst
License:	BSD
Source0:	http://www.w3.org/People/Raggett/%{name}%{version}.tgz
URL:		http://www.w3.org/People/Raggett/tidy/
#Patch0:		%{name}30apr00-html.patch
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

%prep
%setup -q -n %{name}%{version}
#%patch

%build
%{__make} CFLAGS="$RPM_OPT_FLAGS"
cp man_page.txt tidy.1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install -s tidy ${RPM_BUILD_ROOT}%{_bindir}
install tidy.1 ${RPM_BUILD_ROOT}%{_mandir}/man1
gzip -9nf ${RPM_BUILD_ROOT}%{_mandir}/man1/* \
	Overview.html release-notes.html

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Overview.html.gz release-notes.html.gz grid.gif tidy.gif
%{_mandir}/man1/*
%attr(755,root,root) %{_bindir}/tidy

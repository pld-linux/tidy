# $Revision: 1.2 $ $Date: 1999-12-09 19:40:09 $
Summary:	Utility to clean up and pretty print HTML files
Summary(pl): Narzêdzie do porz±dkowania kodu HTML
Name:		tidy
Version:	30nov99
Release:	1
Group:		Utilities/Text
Group(pl):	Narzêdzia/Tekst
Copyright:  BSD
Source:		http://www.w3.org/People/Raggett/%{name}%{version}.tgz
URL:        http://www.w3.org/People/Raggett/tidy/
Patch:      %{name}%{version}-html.patch.gz
Buildroot:	/tmp/%{name}-%{version}-root

%description
Tidy is utility for cleaning and pretty printing HTML files. It can help
in keeping your WWW sources in unified format (case of tags) and proper
encoding of different character sets.

%description -l pl
Tidy jest narzêdziem s³u¿±cym do czytelnego formatowania i wy¶wietlania
¼ród³owego kodu HTML. U³atwia utrzymanie porz±dku w ¼ród³ach stron WWW,
utrzymanie jednolitej konwecji (wielko¶æ liter w tagach) oraz poprawnego
kodowania ró¿nych standardów znaków.

%prep
%setup -q -n %{name}%{version}
%patch

%build
make CFLAGS="${RPM_OPT_FLAGS}"
cp man_page.txt tidy.1

%install
install -d ${RPM_BUILD_ROOT}%{_bindir}
install -s tidy ${RPM_BUILD_ROOT}%{_bindir}
install -d ${RPM_BUILD_ROOT}%{_mandir}/man1
install tidy.1 ${RPM_BUILD_ROOT}%{_mandir}/man1
gzip -9nf ${RPM_BUILD_ROOT}%{_mandir}/man1/*
gzip -9nf Overview.html release-notes.html

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(644,root,root,755)
%doc Overview.html.gz release-notes.html.gz grid.gif tidy.gif
%{_mandir}/man1/*
%attr(755,root,root) %{_bindir}/tidy

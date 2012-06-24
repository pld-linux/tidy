# $Revision: 1.1 $ $Date: 1999-12-09 19:00:39 $
Summary:	Utility to clean up and pretty print HTML files
Summary(pl): Narz�dzie do porz�dkowania kodu HTML
Name:		tidy
Version:	30nov99
Release:	1
Group:		Utilities/Text
Group(pl):	Narz�dzia/Tekst
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
Tidy jest narz�dziem s�u��cym do czytelnego formatowania i wy�wietlania
�r�d�owego kodu HTML. U�atwia utrzymanie porz�dku w �r�d�ach stron WWW,
utrzymanie jednolitej konwecji (wielko�� liter w tagach) oraz poprawnego
kodowania r�nych standard�w znak�w.

%prep
%setup -q -n %{name}%{version}
%patch

%build
make CFLAGS="${RPM_OPT_FLAGS}"
cp man_page.txt tidy.1

%install
install -d ${RPM_BUILD_ROOT}/usr/bin
install -s tidy ${RPM_BUILD_ROOT}/usr/bin
install -d ${RPM_BUILD_ROOT}/usr/man/man1
install tidy.1 ${RPM_BUILD_ROOT}/usr/man/man1

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(644,root,root,755)
%doc Overview.html release-notes.html grid.gif tidy.gif
%doc /usr/man/man1/tidy.1
%attr(755,root,root) /usr/bin/tidy

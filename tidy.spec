# $Revision: 1.12 $ $Date: 2001-05-03 01:14:03 $
Summary:	Utility to clean up and pretty print HTML files
Summary(pl):	Narz�dzie do porz�dkowania kodu HTML
Name:		tidy
Version:	4aug00
Release:	1
Epoch:		1
Group:		Applications/Text
Group(de):	Applikationen/Text
Group(pl):	Aplikacje/Tekst
License:	BSD
Source0:	http://www.w3.org/People/Raggett/%{name}%{version}.tgz
URL:		http://www.w3.org/People/Raggett/tidy/
#Patch0:	%{name}30apr00-html.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tidy is utility for cleaning and pretty printing HTML files. It can
help in keeping your WWW sources in unified format (case of tags) and
proper encoding of different character sets.

%description -l pl
Tidy jest narz�dziem s�u��cym do czytelnego formatowania i
wy�wietlania �r�d�owego kodu HTML. U�atwia utrzymanie porz�dku w
�r�d�ach stron WWW, utrzymanie jednolitej konwecji (wielko�� liter w
tagach) oraz poprawnego kodowania r�nych standard�w znak�w.

%prep
%setup -q -n %{name}%{version}
#%patch

%build
%{__make} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install tidy ${RPM_BUILD_ROOT}%{_bindir}
install man_page.txt ${RPM_BUILD_ROOT}%{_mandir}/man1/tidy.1
gzip -9nf Overview.html release-notes.html

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Overview.html.gz release-notes.html.gz grid.gif tidy.gif
%{_mandir}/man1/*
%attr(755,root,root) %{_bindir}/tidy

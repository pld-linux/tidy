# $Revision: 1.17 $ $Date: 2002-02-22 23:29:48 $
%define w3cver 4aug00
Summary:	Utility to clean up and pretty print HTML files
Summary(pl):	Narzêdzie do porz±dkowania kodu HTML
Name:		tidy
Version:	20000804.%{w3cver}
Release:	1
License:	BSD
Group:		Applications/Text
Source0:	http://www.w3.org/People/Raggett/%{name}%{w3cver}.tgz
URL:		http://www.w3.org/People/Raggett/tidy/
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
%setup -q -n %{name}%{w3cver}

%build
%{__make} CFLAGS="%{rpmcflags}"
cp man_page.txt tidy.1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install tidy ${RPM_BUILD_ROOT}%{_bindir}
install tidy.1 ${RPM_BUILD_ROOT}%{_mandir}/man1

gzip -9nf Overview.html release-notes.html

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Overview.html.gz release-notes.html.gz grid.gif tidy.gif
%{_mandir}/man1/*
%attr(755,root,root) %{_bindir}/tidy

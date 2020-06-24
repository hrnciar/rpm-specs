Name:           mediawiki-intersection
Version:        37906
Release:        13%{?dist}
Summary:        Create a list of pages that are listed in a set of categories

License:        GPLv2+
URL:            http://www.mediawiki.org/wiki/Extension:DynamicPageList_(Wikimedia)
Source0:        http://upload.wikimedia.org/ext-dist/intersection-MW1.13-37906.tar.gz
BuildArch:      noarch

Requires:       mediawiki >= 1.5

%description
Outputs a bulleted list of most recent items
residing in a category, or an intersection
of several categories.
DynamicPageList is another name for this extension.

%prep
%setup -q -n intersection

%post
echo 'To complete installation of %{name}, add the following lines to LocalSettings.php:

    require_once("$IP/extensions/intersection/DynamicPageList.php");

for each MediaWiki instance you wish to install %{name} on.' > README.fedora

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/mediawiki/extensions/intersection/
install -cpm 644 %{_builddir}/%{buildsubdir}/* %{buildroot}%{_datadir}/mediawiki/extensions/intersection/

%files
%{_datadir}/mediawiki/extensions/intersection

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 37906-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 37906-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 37906-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 37906-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 37906-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 37906-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 37906-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 37906-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 37906-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 37906-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 37906-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 37906-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Aug 25 2012 Patrick Uiterwijk <puiterwijk@gmail.com> - 37906-1
- First packaging effort

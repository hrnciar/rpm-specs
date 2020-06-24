# Linked to the version of mediawiki in each Fedora release.
# Rawhide has 1.33, so we package the latest commit in the REL_1_33 branch.
# For non rawhide releases, this will change accordingly
# Remember to ensure that the upgrade path is maintained
%global commit be28231ebcd539fc99775811e5dc6df9064cfa94

%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global reponame mediawiki-extensions-LastModified

Name:           mediawiki-lastmodified
Version:        0
Release:        0.3.20200210git%{commit}%{?dist}
Summary:        Show the last modified page time

License:        GPLv2+
URL:            https://www.mediawiki.org/wiki/Extension:LastModified
Source0:        https://github.com/wikimedia/%{reponame}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
BuildArch:      noarch

Requires:       mediawiki >= 1.33, mediawiki < 1.34

%description
The LastModified extension displays text on the page showing the last modified
page time.

%prep
%autosetup -n %{reponame}-%{commit}
# Remove unneeded dotfiles
rm ./{.gitignore,.gitreview,.jshintrc} -v

%build
# Nothing here

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/mediawiki/extensions/LastModified/{i18n,modules}
install -cpm 644 ./LastModified.php $RPM_BUILD_ROOT%{_datadir}/mediawiki/extensions/LastModified/
install -cpm 644 ./i18n/* $RPM_BUILD_ROOT%{_datadir}/mediawiki/extensions/LastModified/i18n/
install -cpm 644 ./modules/* $RPM_BUILD_ROOT%{_datadir}/mediawiki/extensions/LastModified/i18n/
install -cpm 644 ./*js $RPM_BUILD_ROOT%{_datadir}/mediawiki/extensions/LastModified/
install -cpm 644 ./*json $RPM_BUILD_ROOT%{_datadir}/mediawiki/extensions/LastModified/
install -cpm 644 ./*md $RPM_BUILD_ROOT%{_datadir}/mediawiki/extensions/LastModified/


%files
%{_datadir}/mediawiki/extensions/LastModified


%changelog
* Tue Feb 11 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0-0.3.20200210gitbe28231ebcd539fc99775811e5dc6df9064cfa94
- Fix versioning in requires
- remove unneeded line in install section
- include all files

* Mon Feb 10 2020 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0-0.1.20200210gitbe28231ebcd539fc99775811e5dc6df9064cfa94
- Initial rpm build

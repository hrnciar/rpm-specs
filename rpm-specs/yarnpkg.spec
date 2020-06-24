%global npm_name yarn
# name yarn would probably confict with cmdtest and hadoop-yarn
# https://bugzilla.redhat.com/show_bug.cgi?id=1507312
%global old_name nodejs-yarn

%{?nodejs_find_provides_and_requires}

%global enable_tests 1

# don't require bundled modules
%global __requires_exclude_from ^%{nodejs_sitelib}/yarn/.*$

Name:           yarnpkg
Version:        1.22.4
Release:        2%{?dist}
Summary:        Fast, reliable, and secure dependency management.
URL:            https://github.com/yarnpkg/yarn
# we need tarball with node_modules
Source0:        %{name}-v%{version}-bundled.tar.gz
Source1:        yarnpkg-tarball.sh
License:        BSD

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging
BuildRequires:  npm

# Package was renamed when Fedora 33 was rawhide
# Don't remove this before Fedora 35
Obsoletes:      %{old_name} < 1.22.4-1
Provides:       %{old_name} = %{version}-%{release}

%description
Fast, reliable, and secure dependency management.


%prep
%setup -q -n %{npm_name}-%{version}

%build
# use build script
npm run build

# remove build dependencies from node_modules
npm prune --production

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json lib bin node_modules \
    %{buildroot}%{nodejs_sitelib}/%{npm_name}

mkdir -p %{buildroot}%{_bindir}
ln -sfr %{buildroot}%{nodejs_sitelib}/%{npm_name}/bin/yarn.js %{buildroot}%{_bindir}/yarnpkg
ln -sfr %{buildroot}%{nodejs_sitelib}/%{npm_name}/bin/yarn.js %{buildroot}%{_bindir}/yarn
ln -sfr %{buildroot}%{nodejs_sitelib}/%{npm_name}/bin/yarn.js %{buildroot}%{_bindir}/%{fc_name}

# Remove executable bits from bundled dependency tests
find %{buildroot}%{nodejs_sitelib}/%{npm_name}/node_modules \
    -ipath '*/test/*' -type f -executable \
    -exec chmod -x '{}' +

%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
if [[ $(%{buildroot}%{_bindir}/yarnpkg --version) == %{version} ]] ; then echo PASS; else echo FAIL && exit 1; fi
if [[ $(%{buildroot}%{_bindir}/yarn --version) == %{version} ]] ; then echo PASS; else echo FAIL && exit 1; fi
if [[ $(%{buildroot}%{_bindir}/%{fc_name} --version) == %{version} ]] ; then echo PASS; else echo FAIL && exit 1; fi
%endif


%files
%doc README.md
%license LICENSE
%{_bindir}/yarnpkg
%{_bindir}/yarn
%{_bindir}/%{fc_name}
%{nodejs_sitelib}/%{npm_name}

%changelog
* Mon Jun 22 2020 Neal Gompa <ngompa13@gmail.com> - 1.22.4-2
- Ensure Obsoletes + Provides stanza takes effect
- Fix broken author identity in changelog entries

* Tue Apr 14 2020 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.22.4-1
- Rename to yarnpkg, remove symlink-deps macro
- Update to 1.22.4

* Mon Jan 27 2020 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.21.1-1
- Resolves: RHBZ#1627748, #1687099, #1788329
- Update to 1.21.1
- Provides /usr/bin/yarn
- Resolves CVE-2019-10773

* Thu Dec 05 2019 Neal Gompa <ngompa@datto.com> - 1.13.0-4
- Rename nodejs-yarn binary package to yarnpkg (similar to other distros)
- Use nodejs macros consistently throughout spec
- Make the tests fail the build if the tests fail

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 13 2019 Jan Staněk <jstanek@redhat.com> - 1.13.0-2
- Remove executable bits from bundled tests
- Related: rhbz#1674073

* Thu Feb 07 2019 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.13.0-1
- Update

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 30 2018 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.9.2-1
- Update to 1.9.2

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 24 2018 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.7.0-1
- Update to 1.7.0

* Wed May 09 2018 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.6.0-1
- Rebase, rebuild with new packaging

* Wed Mar 21 2018 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.5.1-2
- Add requires_exclude_from macro
- rename nodejs-yarnpkg to yarn

* Wed Mar 21 2018 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.5.1-1
- Rebase

* Tue Jan 30 2018 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.4.1-1
- rebase
- package from GH, build with npm

* Tue Dec 05 2017 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.3.2-2
- Add fedora readme so users are able to find renamed commands
- change source url
- rename license according to guidelines

* Mon Nov 27 2017 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.3.2-1
- Initial build

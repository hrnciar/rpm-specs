# spec file for package nodejs-nodejs-ansi-regex

%global npm_name ansi-regex

%{?nodejs_find_provides_and_requires}

# Disable tests due to missing npm(ava)
%bcond_with tests

Name:           nodejs-ansi-regex
Version:        2.1.1
Release:        1%{?dist}
Summary:        Regular expression for matching ANSI escape codes
URL:            https://github.com/sindresorhus/ansi-regex
Source0:        https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
# The test files are not included in the npm tarball.
Source1:        https://raw.githubusercontent.com/chalk/ansi-regex/%{version}/test.js

License:        MIT
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs

%if %{with tests}
BuildRequires: npm(ava)
%endif

%description
Regular expression for matching ANSI escape codes

%prep
%setup -q -n package
cp -p %{SOURCE1} "${PWD}"

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json index.js \
  %{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%check
%{nodejs_symlink_deps} --check
%{__nodejs} -e 'require("./")'
%if %{with tests}
%{_bindir}/ava --verbose
%endif

%files
%{nodejs_sitelib}/ansi-regex

%doc readme.md
%license license

%changelog
* Thu Aug 06 2020 Jan Staněk <jstanek@redhat.com> - 2.1.1-1
- Upgrade to 2.1.1 to trim down dependencies

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-12
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 12 2016 Piotr Popieluch <piotr1212@gmail.com> - 2.0.0-2
- Remove deprecated BR: nodejs-devel
- Fix space/tab mixing

* Thu Oct 22 2015 Jared Smith <jsmith@fedoraproject.org> - 2.0.0-1
- Update to upstream 2.0.0 release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 13 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.1.1-1
- Initial build

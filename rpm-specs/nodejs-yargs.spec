# This macro is needed at the start for building on EL6
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

%global barename yargs

Name:               nodejs-yargs
Version:            3.2.1
Release:            12%{?dist}
Summary:            Light-weight option parsing with an argv hash

License:            MIT
URL:                https://www.npmjs.org/package/yargs
Source0:            http://registry.npmjs.org/%{barename}/-/%{barename}-%{version}.tgz
BuildArch:          noarch
%if 0%{?fedora} >= 19
ExclusiveArch:      %{nodejs_arches} noarch
%else
ExclusiveArch:      %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:      nodejs-packaging >= 6

%if 0%{?enable_tests}
BuildRequires:      npm(hashish)
BuildRequires:      npm(chai)
BuildRequires:      npm(mocha)
%endif


%description
Yargs be a node.js library fer hearties tryin' ter parse optstrings against
their will where even the boo box be not enough to coerce them. This here
module is fer scallywags lookin' ter plunder all the sunken -shipz of their
--treasures thru program usage but be tired of optstrings disincling to
acquiesce to yer requests.

With yargs, ye be havin' a map that leads straight to yer treasure! Treasure of
course, being a simple option hash.

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep --caret
%nodejs_fixdep wordwrap

%build
%nodejs_symlink_deps --build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/yargs
cp -pr package.json lib index.js \
    %{buildroot}%{nodejs_sitelib}/yargs

%nodejs_symlink_deps


%check
%if 0%{?enable_tests}
%nodejs_symlink_deps --check
mocha -R nyan
%endif


%files
%doc README.md LICENSE
%{nodejs_sitelib}/yargs/

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Feb 16 2016 Jared Smith <jsmith@fedoraproject.org> - 3.2.1-5
- Relax version of npm(wordwrap)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov 15 2015 Piotr Popieluch <piotr1212@gmail.com> - 3.2.1-3
- Remove unused dependency

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Feb 22 2015 Ralph Bean <rbean@redhat.com> - 3.2.1-1
- new version

* Fri Feb 20 2015 Ralph Bean <rbean@redhat.com> - 3.1.0-1
- new version

* Fri Jan 09 2015 Ralph Bean <rbean@redhat.com> - 1.3.3-1
- Update to latest upstream for RHBZ#1177619.

* Tue Jul 22 2014 Ralph Bean <rbean@redhat.com> - 1.2.6-1
- Initial packaging for Fedora.

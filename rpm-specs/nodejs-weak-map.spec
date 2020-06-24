%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:       nodejs-weak-map
Version:    1.0.5
Release:    10%{?dist}
Summary:    A WeakMap shim for Node.js and browsers
License:    ASL 2.0
URL:        https://github.com/drses/weak-map
Source0:    http://registry.npmjs.org/weak-map/-/weak-map-%{version}.tgz
# Source1 is generated by running Source10, which pulls from the upstream
# version control repository.
Source1:    tests-v%{version}.tar.bz2
Source10:   dl-tests.sh

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  nodejs-packaging

%description
WeakMap is a collection introduced to JavaScript with EcmaScript 6. It
provides a mapping from objects to values, but allows any entry to be
garbage collected if the key is provably lost.

In order for it to be possible that a key is provably lost, weak maps
do not provide a way to access the key list.

This is a Node.js module that provides a shim and patcher for missing
or broken WeakMap implementations, suitable for use in Node.js and
browsers that provide the EcmaScript 5 property description interfaces.


%prep
%setup -q -n package
%setup -q -T -D -a 1 -n package


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/weak-map
cp -pr package.json weak-map.js \
    %{buildroot}%{nodejs_sitelib}/weak-map

%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
#  /usr/bin/npm install jasminum@^2.0.1
#  mkdir -p node_modules/jasminum/node_modules/collections/node_modules
#  ln -sf %%{_builddir}/package \
#     node_modules/jasminum/node_modules/collections/node_modules/weak-map
%__nodejs --harmony_collections test/index.js
%__nodejs test/index.js
%endif


%files
%doc README.md
%{nodejs_sitelib}/weak-map


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 28 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.0.5-1
- update to upstream release 1.0.5
- tests have been removed from NPM tarball so download separately

* Sat Apr 19 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.0.4-1
- initial package

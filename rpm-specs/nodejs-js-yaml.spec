%{?nodejs_find_provides_and_requires}

%global enable_tests 1

Name:           nodejs-js-yaml
Version:        3.10.0
Release:        6%{?dist}
Summary:        YAML 1.2 parser and serializer

License:        MIT
URL:            https://github.com/nodeca/js-yaml
Source0:        https://registry.npmjs.org/js-yaml/-/js-yaml-%{version}.tgz
# The test/ directory is not included in the npm tarball.
# Source1 is generated by running Source10, which pulls from the upstream
# revision control repository.
Source1:        tests-%{version}.tar.bz2
Source2:        examples-%{version}.tar.bz2
Source10:       dl-tests.sh

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(esprima)
BuildRequires:  npm(mocha)
%endif

%description
This is an implementation of YAML (YAML Ain't Markup Language), a human
friendly data serialization language. It started as PyYAML port, and was
completely rewritten from scratch.  Now it's very fast, and supports the
1.2 spec.


%prep
%setup -q -n package
%setup -q -T -D -a 1 -n package
%setup -q -T -D -a 2 -n package

sed -i '1s/env //' bin/js-yaml.js

%nodejs_fixdep esprima


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/js-yaml
cp -pr package.json index.js lib/ \
    %{buildroot}%{nodejs_sitelib}/js-yaml

mkdir -p %{buildroot}%{nodejs_sitelib}/js-yaml/bin
install -p -D -m0755 bin/js-yaml.js \
    %{buildroot}%{nodejs_sitelib}/js-yaml/bin/js-yaml.js
mkdir -p %{buildroot}%{_bindir}
ln -sf %{nodejs_sitelib}/js-yaml/bin/js-yaml.js \
    %{buildroot}%{_bindir}/js-yaml

%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
NODE_ENV=test %{_bindir}/mocha -R spec
%endif


%files
%{!?_licensedir:%global license %doc}
%doc README.md CHANGELOG.md examples/
%license LICENSE
%{nodejs_sitelib}/js-yaml
%{_bindir}/js-yaml


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Sep 20 2017 Jared Smith <jsmith@fedoraproject.org> - 3.10.0-1
- Update to upstream 3.10.0 release

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jul 25 2016 Jared Smith <jsmith@fedoraproject.org> - 3.6.1-1
- Update to upstream 3.6.1 release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 11 2016 Tom Hughes <tom@compton.nu> - 3.5.2-2
- Update dependencies

* Mon Jan 11 2016 Tom Hughes <tom@compton.nu> - 3.5.2-1
- Update to 3.5.2 upstream release

* Mon Jan 11 2016 Tom Hughes <tom@compton.nu> - 3.5.0-1
- Update to 3.5.0 upstream release

* Fri Jan  1 2016 Tom Hughes <tom@compton.nu> - 3.4.6-1
- Update to 3.4.6 upstream release

* Fri Dec  4 2015 Tom Hughes <tom@compton.nu> - 2.1.3-4
- Update npm(argparse) dependency

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 18 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 2.1.3-1
- update to upstream release 2.1.3

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild
- also since the last EL6 build got garbage collected

* Sun Jul 21 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 2.1.0-2
- add logic for ExclusiveArch macro

* Fri Jun 21 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 2.1.0-1
- initial package

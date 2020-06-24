%{?nodejs_find_provides_and_requires}

%global enable_tests 1

Name:       nodejs-fileset
Version:    0.2.1
Release:    11%{?dist}
Summary:    A wrapper around glob and minimatch for Node.js
License:    MIT
URL:        https://github.com/mklabs/node-fileset
Source0:    https://registry.npmjs.org/fileset/-/fileset-%{version}.tgz

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(glob)
%endif

%description
This Node.js module exposes a basic wrapper on top of nodejs-glob and
nodejs-minimatch. It adds multiple patterns matching and allows a list
of include patterns and optional exclude patterns.


%prep
%setup -q -n package
%nodejs_fixdep glob
%nodejs_fixdep minimatch


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/fileset
cp -pr package.json lib/ \
    %{buildroot}%{nodejs_sitelib}/fileset

%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
%__nodejs ./tests/test.js && %__nodejs ./tests/test-sync.js
%endif


%files
%doc README.md CHANGELOG.md
%license LICENSE-MIT
%{nodejs_sitelib}/fileset


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Nov 07 2015 Piotr Popieluch <piotr1212@gmail.com> - 0.2.1-3
- fixdep minimatch

* Sat Nov 07 2015 Piotr Popieluch <piotr1212@gmail.com> - 0.2.1-2
- fixdep glob

* Fri Nov 06 2015 Piotr Popieluch <piotr1212@gmail.com> - 0.2.1-1
- Update to new version

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 21 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.1.5-3
- restrict to compatible arches

* Wed Jun 19 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.5-2
- rebuild for missing npm(fileset) provides on EL6

* Sun Feb 17 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.1.5-1
- initial package

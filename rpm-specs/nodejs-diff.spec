%{?nodejs_find_provides_and_requires}

%global enable_tests 1

Name:       nodejs-diff
Version:    1.0.8
Release:    13%{?dist}
Summary:    A JavaScript text diff implementation for Node.js
# LICENSE text is included in README.md
License:    BSD
URL:        https://github.com/kpdecker/jsdiff
Source0:    http://registry.npmjs.org/diff/-/diff-%{version}.tgz
# Source1 is generated by running Source10, which pulls from the upstream
# revision control repository.
Source1:    tests-v%{version}.tar.bz2
Source10:   dl-tests.sh

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(colors)
BuildRequires:  npm(mocha)
BuildRequires:  npm(should)
%endif

%description
%{summary}


%prep
%setup -q -n package
%setup -q -T -D -a 1 -n package


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/diff
cp -pr package.json diff.js \
    %{buildroot}%{nodejs_sitelib}/diff

%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
%{nodejs_sitelib}/mocha/bin/mocha test/*.js
%endif


%files
%doc README.md
%{nodejs_sitelib}/diff


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-13
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 18 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.0.8-1
- update to upstream release 1.0.8

* Tue Sep 03 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.0.6-1
- update to upstream release 1.0.6

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 21 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.0.5-1
- update to upstream release 1.0.5
- restrict to compatible arches
- test/ directory has been excluded from the npm tarball, so d/l separately

* Wed Jun 19 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.4-2
- rebuild for missing npm(diff) provides on EL6

* Thu Feb 14 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.0.4-1
- initial package

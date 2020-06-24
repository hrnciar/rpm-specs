%{?nodejs_find_provides_and_requires}
%global enable_tests 1

Name:       nodejs-i18n-transform
Version:    2.1.3
Release:    9%{?dist}
Summary:    i18n transforms to a json object.
License:    MIT
URL:        https://github.com/andyroyle/i18n-transform
Source:     http://registry.npmjs.org/i18n-transform/-/i18n-transform-%{version}.tgz
Patch0:     nodejs-i18n-transform-lodash3.patch

BuildArch:  noarch

BuildRequires:  nodejs-packaging

ExclusiveArch: %{nodejs_arches} noarch

%if 0%{?enable_tests}
BuildRequires:  npm(mocha)
BuildRequires:  npm(should)
BuildRequires:  npm(lodash)
%endif

%description
i18n transforms to a json object.

%prep
%autosetup -p 1 -n package


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/i18n-transform
cp -pr Gruntfile.js index.js package.json lib/ \
    %{buildroot}%{nodejs_sitelib}/i18n-transform


%check
%if 0%{?enable_tests}
%nodejs_symlink_deps --check
%{nodejs_sitelib}/mocha/bin/mocha -R spec tests/tests.js
%endif

%files
%doc README.md tests/
%license LICENSE
%{nodejs_sitelib}/i18n-transform


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Oct 19 2016 Tom Hughes <tom@compton.nu> - 2.1.3-2
- Patch to work with lodash 3.x
- Enable tests

* Mon Oct 17 2016 Anish Patil <anish.developer@gmail.com> - 2.1.3-1
- Upstream has released new tarball

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Sep 18 2014 Anish Patil <apatil@redhat.com> - 1.1.1-1
- Upstream has released new tarball

* Tue Aug 19 2014 Anish Patil <apatil@redhat.com> - 1.0.2-1
- Upstream has released new tarball

* Tue Jul 22 2014 Anish Patil <apatil@redhat.com> - 1.0.1-2
- Incorporated package review comments

* Fri May 09 2014 Anish Patil <apatil@redhat.com> - 1.0.1-1
- Initial package

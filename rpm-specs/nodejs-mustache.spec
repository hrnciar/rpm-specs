%{?nodejs_find_provides_and_requires}
%global enable_tests 0

Name:       nodejs-mustache
Version:    2.2.1
Release:    8%{?dist}
Summary:    mustache.js is an implementation of the mustache template system in JavaScript
License:    MIT
URL:        https://github.com/janl/mustache.js
Source:     http://registry.npmjs.org/mustache/-/mustache-%{version}.tgz


BuildArch:  noarch

BuildRequires:  nodejs-packaging
ExclusiveArch: %{nodejs_arches} noarch

%if 0%{?enable_tests}
BuildRequires:  npm(mocha)
%endif

%description
An implementation of the mustache template system in JavaScript.Mustache is a logic-less template syntax. It can be used for HTML, config files, source code - anything. It works by expanding tags in a template using values provided in a hash or object.
We call it "logic-less" because there are no if statements, else clauses, or for loops. Instead there are only tags. Some tags are replaced with a value, some nothing, and others a series of values.

%prep
%setup -q -n package



%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/mustache
cp -pr mustache.js  package.json mustache.min.js wrappers/ \
    %{buildroot}%{nodejs_sitelib}/mustache
%nodejs_symlink_deps 

%if 0%{?enable_tests}
%check
mocha test
%endif

%files
%doc LICENSE CHANGELOG.md README.md 
%{nodejs_sitelib}/mustache


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 17 2016 Anish Patil <anish.developer@gmail.com> - 2.2.1-1
- Upstream has released new version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Feb 06 2015 Anish Patil <apatil@redhat.com> - 1.0.0-2
- Build with few minor changes
* Wed Dec 24 2014 Anish Patil <apatil@redhat.com> - 1.0.0-1
- Upstream has released new version
* Thu Sep 04 2014 Anish Patil <apatil@redhat.com> - 0.8.2-1
- Initial package

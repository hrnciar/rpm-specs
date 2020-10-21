%{?nodejs_find_provides_and_requires}

Name:       nodejs-sprintf
Version:    0.1.5
Release:    11%{?dist}
Summary:    JavaScript sprintf implementation 
License:    MIT
URL:        https://github.com/maritz/node-sprintf
Source:     http://registry.npmjs.org/sprintf/-/sprintf-%{version}.tgz


BuildArch:  noarch

BuildRequires:  nodejs-packaging
ExclusiveArch: %{nodejs_arches} noarch

%description
Sprintf is a JavaScript sprintf implementation for node.js

%prep
%setup -q -n package
%nodejs_fixdep --caret

%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/sprintf
cp -pr package.json lib/ \
    %{buildroot}%{nodejs_sitelib}/sprintf
%nodejs_symlink_deps 



%files
%doc README.md test/
%{nodejs_sitelib}/sprintf


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Feb 06 2015 Anish Patil <apatil@redhat.com> - 0.1.5-1
- Upstream has released new version

* Tue Aug 19 2014 Anish Patil <apatil@redhat.com> - 0.1.4-1
- Upstream has released new version

* Wed Jul 23 2014 Anish Patil <apatil@redhat.com> - 0.1.3-3
- Incorporated package review comments

* Tue Jul 22 2014 Anish Patil <apatil@redhat.com> - 0.1.3-2
- Incorporated package review comments

* Fri May 09 2014 Anish Patil <apatil@redhat.com> - 0.1.3-1
- Initial package

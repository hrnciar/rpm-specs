%{?nodejs_find_provides_and_requires}

Name:       nodejs-strip-json-comments
Version:    2.0.1
Release:    9%{?dist}
Summary:    Strip comments from JSON
License:    MIT
URL:        https://github.com/sindresorhus/strip-json-comments
Source:     https://github.com/sindresorhus/strip-json-comments/archive/v%{version}.tar.gz



BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging


%description
Strip comments from JSON. Lets you use comments in your JSON files!


%prep
%setup -q -n strip-json-comments-%{version}




%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/strip-json-comments
cp -pr package.json index.js \
    %{buildroot}%{nodejs_sitelib}/strip-json-comments




%nodejs_symlink_deps



%files
%doc readme.md license
%{nodejs_sitelib}/strip-json-comments



%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 17 2016 Anish Patil <anish.developer@gmail.com> - 2.0.1-1
- Upstream has released new version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Oct 19 2014 Anish Patil <apatil@redhat.com> - 1.0.2-1
- Upstream has released new version

* Tue Aug 19 2014 Anish Patil <apatil@redhat.com> - 1.0.1-1
- Upstream has released new version

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jun 4 2014 Anish Patil <apatil@redhat.com> - 0.1.3-4
- Incorporated package review comments

* Wed May 28 2014 Anish Patil <apatil@redhat.com> - 0.1.2-3
- Incorporated package review comments

* Wed May 07 2014 Anish Patil <apatil@redhat.com> - 0.1.1-2
- Incorporated package review comments

* Thu Apr 10 2014 Anish Patil <apatil@redhat.com> - 0.1.1-1
- Initial package

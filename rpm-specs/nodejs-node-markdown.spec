Name:           nodejs-node-markdown
Version:        0.1.1
Release:        13%{?dist}
Summary:        Parse markdown syntax with Node.js

License:        BSD
URL:            https://github.com/andris9/node-markdown
Source0:        http://registry.npmjs.org/node-markdown/-/node-markdown-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging
Requires:       npm(showdown)

%description
Based on showdown parser and parses markdown syntax into HTML code.


%prep
%setup -q -n package
rm -rf node_modules lib/vendor


%build


%install
mkdir -p %{buildroot}/%{nodejs_sitelib}/node-markdown
cp -pr package.json lib %{buildroot}/%{nodejs_sitelib}/node-markdown
mkdir -p %{buildroot}/%{nodejs_sitelib}/node-markdown/lib/vendor
ln -sf %{nodejs_sitelib}/showdown %{buildroot}/%{nodejs_sitelib}/node-markdown/lib/vendor
%nodejs_symlink_deps


%files
%doc LICENSE README.md examples
%{nodejs_sitelib}/node-markdown


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 16 2013 Tom Hughes <tom@compton.nu> - 0.1.1-2
- Link showdown to lib/vendor instead of patching paths
- Update to latest nodejs packaging standards

* Sun Feb 10 2013 Tom Hughes <tom@compton.nu> - 0.1.1-1
- Initial build of 0.1.1

Name:       nodejs-codemirror
Version:    5.51.0
Release:    3%{?dist}
Summary:    A versatile JS text editor
License:    MIT
URL:        http://codemirror.net/
Source0:    http://registry.npmjs.org/codemirror/-/codemirror-%{version}.tgz
BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

%description
CodeMirror is a JavaScript component that provides a code editor in
the browser. When a mode is available for the language you are coding
in, it will color your code, and optionally help with indentation.

%prep
%setup -q -n package
rm -rf node_modules

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/codemirror
cp -pr addon lib mode package.json theme bin keymap rollup.config.js src %{buildroot}%{nodejs_sitelib}/codemirror

%nodejs_symlink_deps


%files
%{nodejs_sitelib}/codemirror
%doc README.md AUTHORS CONTRIBUTING.md CHANGELOG.md
%license LICENSE

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.51.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.51.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 22 2020 Mosaab Alzoubi <moceap@hotmail.com> - 5.51.0-1
- Update to 5.51.0
- Use license macro

* Tue Aug 27 2019 Mosaab Alzoubi <moceap@hotmail.com> - 5.48.4-1
- Update to 5.48.4

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Nov 25 2014 Mosaab Alzoubi <moceap@hotmail.com> - 4.8.0-1
- Update to 4.8.0

* Fri Oct 24 2014 Mosaab Alzoubi <moceap@hotmail.com> - 4.6.0-3
- Fix shebang warnings

* Wed Oct 22 2014 Mosaab Alzoubi <moceap@hotmail.com> - 4.6.0-2
- General revision.

* Thu Sep 25 2014 Mosaab Alzoubi <moceap@hotmail.com> - 4.6.0-1
- Update to 4.6

* Sun Dec 1 2013 Mosaab Alzoubi <moceap@hotmail.com> - 3.20.0-1
- Initial packaging.

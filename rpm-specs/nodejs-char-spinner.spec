%{?scl:%scl_package nodejs-char-spinner}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

Name:		%{?scl_prefix}nodejs-char-spinner
Version:	1.0.1
Release:	15%{?dist}
Summary:	Node.js char spinner
License:	ISC
Url:		https://github.com/isaacs/char-spinner
Source0:	http://registry.npmjs.org/char-spinner/-/char-spinner-%{version}.tgz
# Cached development dependencies
# $ npm install --save-dev && tar -czf ../char-spinner-%%{version}-node_modules.tar.gz node_modules
Source1:	char-spinner-%{version}-node_modules.tar.gz
BuildRequires:	nodejs-packaging nodejs(engine)
BuildArch:	noarch
ExclusiveArch:	%{nodejs_arches} noarch

%description
Put a little spinner on process.stderr, as unobtrusively as possible.

%prep
%autosetup -n package
tar -xzf "%{SOURCE1}"

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/char-spinner
cp -pr package.json spin.js \
	%{buildroot}%{nodejs_sitelib}/char-spinner

%{nodejs_symlink_deps}

%check
%{nodejs_symlink_deps} --check
%{__nodejs} ./node_modules/tap/bin/tap.js test/*.js

%files
%doc README.md
%{nodejs_sitelib}/char-spinner
%license LICENSE

%changelog
* Mon Aug 17 2020 Jan Staněk <jstanek@redhat.com> - 1.0.1-15
- Cache development dependencies to resolve FTBFS

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-14
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 10 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.1-3
- Fixed dependency on nodejs-packaging
- added %%nodejs_symlink_deps, %%check and %%license
- changed ExclusiveArch and %%nodejs_find_and_provides
- removed Group, BuildRoot and %%defattr


* Tue Jan 13 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.1-2
- Remove undefined macro

* Mon Jan 12 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.1-1
- Initial build


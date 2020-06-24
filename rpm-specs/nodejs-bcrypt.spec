%{?nodejs_find_provides_and_requires}

%global enable_tests 1

Name:           nodejs-bcrypt
Version:	3.0.8
Release:	1%{?dist}
Summary:	A bcrypt library for NodeJS

License:	MIT
URL:		https://www.npmjs.com/package/bcrypt
Source0:	https://registry.npmjs.org/bcrypt/-/bcrypt-%{version}.tgz
# Patch out use of node-pre-gyp
Patch1:		nodejs-bcrypt-pregyp.patch
ExclusiveArch:  %{nodejs_arches}

BuildRequires:	nodejs-packaging
BuildRequires:	node-gyp
BuildRequires:	nodejs-devel
BuildRequires:	npm(bindings)
BuildRequires:	npm(nan)

%if 0%{?enable_tests}
BuildRequires:	npm(nodeunit)
%endif

%description
A bcrypt library for NodeJS.


%prep
%autosetup -p 1 -n package
%nodejs_fixdep --dev --move nan
rm -rf node_modules


%build
%nodejs_symlink_deps --build
%set_build_flags
node-gyp rebuild
rm -rf node_modules


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/bcrypt
cp -pr package.json *.js lib build %{buildroot}%{nodejs_sitelib}/bcrypt
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
%{_bindir}/nodeunit test
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif


%files
%doc *.md examples/
%license LICENSE
%{nodejs_sitelib}/bcrypt


%changelog
* Thu Feb  6 2020 Tom Hughes <tom@compton.nu> - 3.0.8-1
- Update to 3.0.8 upstream release

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Jared K. Smith <jsmith@fedoraproject.org> - 3.0.6-2
- rebuilt for missing lib dir

* Wed Jul 31 2019 Jared K. Smith <jsmith@fedoraproject.org> - 3.0.6-1
- Update to upstream 3.0.6 release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 14 2019 Tom Hughes <tom@compton.nu> - 0.8.7-15
- Rebuild for Node.js 12.4.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 22 2018 Tom Hughes <tom@compton.nu> - 0.8.7-12
- Rebuild for Node.js 10.5.0

* Thu Mar  8 2018 Tom Hughes <tom@compton.nu> - 0.8.7-10
- Relax npm(bindings) dependency

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Tom Hughes <tom@compton.nu> - 0.8.7-8
- Export LDFLAGS for hardened build support
- Allow undefined symbols in the shared object

* Thu Aug 10 2017 Tom Hughes <tom@compton.nu> - 0.8.7-7.1
- Rebuild for Node.js 8.3.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-6.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-5.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 28 2017 Tom Hughes <tom@compton.nu> - 0.8.7-4.1
- Rebuild for Node.js 8.1.2

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Oct 19 2016 Kalev Lember <klember@redhat.com> - 0.8.7-3
- Rebuild for nodejs(v8-abi) update

* Thu Sep 01 2016 Stephen Gallagher <sgallagh@redhat.com> - 0.8.7-2
- Rebuild for nodejs(v8-abi) update

* Fri Jul  8 2016 Jared Smith <jsmith@fedoraproject.org> - 0.8.7-1
- Initial packaging

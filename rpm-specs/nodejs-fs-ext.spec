%global enable_tests 1
%global module_name fs-ext

Name:           nodejs-%{module_name}
Version:        1.3.0
Release:        3%{?dist}
Summary:        Extensions to core 'fs' module for Node.js

License:        MIT
URL:            https://github.com/baudehlo/node-fs-ext/
Source0:        https://registry.npmjs.org/%{module_name}/-/%{module_name}-%{version}.tgz

BuildRequires:  node-gyp
BuildRequires:  nodejs-devel
BuildRequires:  npm(nan) >= 2.0.0

Requires:       npm(nan)

BuildRequires:  nodejs-packaging
ExclusiveArch:   %{nodejs_arches}

%description
%{summary}.

%prep
%autosetup -n package
rm -rf node_modules
%nodejs_fixdep nan

%build
%nodejs_symlink_deps --build
export CXXFLAGS="%{optflags}"
export LDFLAGS="%{?__global_ldflags} -Wl,-z,undefs"
node-gyp rebuild
rm -rf node_modules

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{module_name}/build
cp -pr fs-ext.js package.json %{buildroot}%{nodejs_sitelib}/%{module_name}
cp -p  build/Release/%{module_name}.node %{buildroot}%{nodejs_sitelib}/%{module_name}/build/
sed -i -e 's|build/Release|build|g' \
    %{buildroot}%{nodejs_sitelib}/%{module_name}/fs-ext.js

# Fix permissions
chmod 755 %{buildroot}%{nodejs_sitelib}/%{module_name}/build/%{module_name}.node

#%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
%{__nodejs} tests/test-fs-fcntl.js
%{__nodejs} tests/test-fs-flock.js
%{__nodejs} tests/test-fs-flock_stress.js
%{__nodejs} tests/test-fs-seek.js
%{__nodejs} tests/test-fs-seek_stress.js
%endif

%files
%doc README.md example.js
%license LICENSE.txt
%{nodejs_sitelib}/%{module_name}

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 15 2019 Tom Hughes <tom@compton.nu> - 1.3.0-1
- Update to 1.3.0 upstream release

* Fri Jun 14 2019 Tom Hughes <tom@compton.nu> - 1.0.0-9
- Rebuild for Node.js 12.4.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 22 2018 Tom Hughes <tom@compton.nu> - 1.0.0-6
- Rebuild for Node.js 10.5.0

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb 05 2018 Jared Smith <jsmith@fedoraproject.org> - 1.0.0-3
- Relax dependency on npm(nan)

* Tue Jan 23 2018 Tom Hughes <tom@compton.nu> - 1.0.0-2
- Export LDFLAGS for hardened build support
- Allow undefined symbols in the shared object

* Wed Sep 20 2017 Parag Nemade <pnemade AT redhat DOT com> - 1.0.0-1
- Update to 1.0.0 version

* Thu Aug 10 2017 Tom Hughes <tom@compton.nu> - 0.6.0-5
- Rebuild for Node.js 8.3.0

* Wed Aug  9 2017 Tom Hughes <tom@compton.nu> - 0.6.0-4
- Patch out failing test

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 28 2017 Tom Hughes <tom@compton.nu> - 0.6.0-1.1
- Rebuild for Node.js 8.1.2

* Sun Mar 12 2017 Parag Nemade <pnemade AT redhat DOT com> - 0.6.0-1
- Update to 0.6.0 version

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-11.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug 29 2016 Tom Hughes <tom@compton.nu> - 0.5.0-10.1
- Rebuild for Node.js 6.5.0

* Mon May 09 2016 Stephen Gallagher <sgallagh@redhat.com> - 0.5.0-9.1
- Rebuild for Node.js 6.1.0 upgrade

* Tue Mar 29 2016 Tom Hughes <tom@compton.nu> - 0.5.0-9
- Rebuild for Node.js 5.x

* Wed Mar 23 2016 Tom Hughes <tom@compton.nu> - 0.5.0-8
- Rebuild for Node.js 4.4.x

* Wed Feb 10 2016 Tom Hughes <tom@compton.nu> - 0.5.0-7
- Rebuild for Node.js 4.3.x

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec  7 2015 Tom Hughes <tom@compton.nu> - 0.5.0-4
- Use %%{nodejs_arches} 

* Fri Dec  4 2015 Tom Hughes <tom@compton.nu> - 0.5.0-3
- Rebuild for nodejs 4.2.3

* Wed Dec  2 2015 Tom Hughes <tom@compton.nu> - 0.5.0-2
- Rebuild for nodejs 4.2

* Mon Nov 23 2015 Tom Hughes <tom@compton.nu> - 0.5.0-1
- Update to 0.5.0 upstream release

* Fri Sep 25 2015 Parag Nemade <pnemade AT redhat DOT com> - 0.4.6-1
- Update to 0.4.6

* Fri Jul 03 2015 Parag Nemade <pnemade AT redhat DOT com> - 0.4.5-1
- Update to 0.4.5

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jan 24 2015 Parag Nemade <pnemade AT redhat DOT com> - 0.4.3-1
- Update to 0.4.3

* Sun Dec 07 2014 Parag Nemade <pnemade AT redhat DOT com> - 0.4.2-2
- enable tests
- fix node file permissions

* Sat Dec 06 2014 Parag Nemade <pnemade AT redhat DOT com> - 0.4.2-1
- Update to 0.4.2
- LICENSE.txt is now added

* Wed Dec 03 2014 Parag Nemade <pnemade AT redhat DOT com> - 0.4.1-1
- Initial packaging


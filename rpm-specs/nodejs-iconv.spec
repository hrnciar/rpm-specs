%{?nodejs_find_provides_and_requires}

Name:           nodejs-iconv
Version:        3.0.0
Release:        1%{?dist}
Summary:        Text recoding in JavaScript for fun and profit

License:        ISC
URL:            https://github.com/bnoordhuis/node-iconv
Source0:        https://registry.npmjs.org/iconv/-/iconv-%{version}.tgz
# Workaround some differences in glibc's iconv vs libiconv
Patch0:         nodejs-iconv-glibc.patch
ExclusiveArch:  %{nodejs_arches}

BuildRequires:  nodejs-devel
BuildRequires:  node-gyp

%{?nodejs_default_filter}


%description
%{summary}.


%prep
%autosetup -p 1 -n package
rm -rf deps support node_modules


%build
%nodejs_symlink_deps --build
export CXXFLAGS="%{optflags}"
export LDFLAGS="%{?__global_ldflags} -Wl,-z,undefs"
node-gyp rebuild -- -Dnode_iconv_use_system_libiconv=1


%install
mkdir -p %{buildroot}%{nodejs_sitearch}/iconv/build/Release
cp -pr package.json index.js %{buildroot}%{nodejs_sitearch}/iconv
install -p -m755 build/Release/iconv.node %{buildroot}%{nodejs_sitearch}/iconv/build/Release
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
mkdir test/tmp
%__nodejs test/run-tests.js


%files
%doc README.md
%license LICENSE
%{nodejs_sitearch}/iconv


%changelog
* Fri Apr 24 2020 Tom Hughes <tom@compton.nu> - 3.0.0-1
- Update to 3.0.0 upstream release

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct  1 2019 Tom Hughes <tom@compton.nu> - 2.3.5-1
- Update to 2.3.5 upstream release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 14 2019 Tom Hughes <tom@compton.nu> - 2.3.4-2
- Rebuild for Node.js 12.4.0

* Sun Mar 31 2019 Tom Hughes <tom@compton.nu> - 2.3.4-1
- Update to 2.3.4 upstream release

* Thu Mar 21 2019 Tom Hughes <tom@compton.nu> - 2.3.3-1
- Update to 2.3.3 upstream release

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 22 2018 Tom Hughes <tom@compton.nu> - 2.3.0-8
- Rebuild for Node.js 10.5.0

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Tom Hughes <tom@compton.nu> - 2.3.0-5
- Allow undefined symbols in the shared object

* Thu Aug 10 2017 Tom Hughes <tom@compton.nu> - 2.3.0-4.1
- Rebuild for Node.js 8.3.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 28 2017 Tom Hughes <tom@compton.nu> - 2.3.0-1.1
- Rebuild for Node.js 8.1.2

* Mon Jun 26 2017 Tom Hughes <tom@compton.nu> - 2.3.0-1
- Update to 2.3.0 upstream release

* Wed Apr  5 2017 Tom Hughes <tom@compton.nu> - 2.2.3-1
- Update to 2.2.3 upstream release

* Tue Apr  4 2017 Tom Hughes <tom@compton.nu> - 2.2.2-1
- Update to 2.2.2 upstream release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug 29 2016 Tom Hughes <tom@compton.nu> - 2.2.1-2
- Rebuild for Node.js 6.5.0

* Thu Jun 16 2016 Tom Hughes <tom@compton.nu> - 2.2.1-1
- Update to 2.2.1 upstream release

* Mon May 09 2016 Stephen Gallagher <sgallagh@redhat.com> - 2.2.0-1.1
- Rebuild for Node.js 6.1.0 upgrade

* Wed Apr 27 2016 Tom Hughes <tom@compton.nu> - 2.2.0-1
- Update to 2.2.0 upstream release

* Tue Mar 29 2016 Tom Hughes <tom@compton.nu> - 2.1.11-8
- Rebuild for Node.js 5.x

* Wed Mar 23 2016 Tom Hughes <tom@compton.nu> - 2.1.11-7
- Rebuild for Node.js 4.4.x

* Wed Feb 10 2016 Tom Hughes <tom@compton.nu> - 2.1.11-6
- Rebuild for Node.js 4.3.x

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec  4 2015 Tom Hughes <tom@compton.nu> - 2.1.11-4
- Rebuild for nodejs 4.2.3

* Wed Dec  2 2015 Tom Hughes <tom@compton.nu> - 2.1.11-3
- Rebuild for nodejs 4.2

* Wed Nov 25 2015 Tom Hughes <tom@compton.nu> - 2.1.11-2
- Fix rpmlint and checksec warnings
- Make npn(nan) a build time dependency only

* Tue Nov 24 2015 Tom Hughes <tom@compton.nu> - 2.1.11-1
- Initial build of 2.1.11

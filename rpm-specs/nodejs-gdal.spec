%{?nodejs_find_provides_and_requires}

Name:           nodejs-gdal
Version:        0.9.9
Release:        4%{?dist}
Summary:        Node.js bindings to GDAL

License:        ASL 2.0
URL:            https://github.com/naturalatlas/node-gdal
# Real source is https://github.com/naturalatlas/node-gdal/archive/v%%{version}/node-gdal-%%{version}.tar.gz
# but files copied from gdal whose provenance is unclear (as described
# in PROVENANCE.TXT and PROVENANCE.TXT-fedora in gdal) have been
# removed from the tar ball by the cleaner script.
Source0:        node-gdal-%{version}-fedora.tar.gz
# Cleaner script for the tarball
Source1:        nodejs-gdal-cleaner.sh
# Use system GDAL
Patch0:         nodejs-gdal-system-gdal.patch
# Don't strip symbols
Patch1:         nodejs-gdal-no-strip.patch
# Patch of use of node-pre-gyp
Patch2:         nodejs-gdal-no-pre-gyp.patch
# https://github.com/naturalatlas/node-gdal/issues/141
Patch3:         nodejs-gdal-threshold.patch
# https://github.com/naturalatlas/node-gdal/pull/259
Patch4:         nodejs-gdal-node12.patch
# Patch gdal 3.0.4 issues
Patch5:         nodejs-gdal-gdal304.patch
# Patch proj 6.x issues
Patch6:         nodejs-gdal-proj6.patch
# Patch gdal 3.1.0 issues
Patch7:         nodejs-gdal_gdal310.patch
ExclusiveArch:  %{nodejs_arches}

BuildRequires:  nodejs-devel
BuildRequires:  node-gyp
BuildRequires:  gdal-devel >= 2.2.0

BuildRequires:  npm(nan) >= 2.5.0
BuildRequires:  npm(mocha)
BuildRequires:  npm(chai)

%{?nodejs_default_filter}


%description
Read and write raster and vector geospatial datasets straight
from Node.js with this native GDAL binding. 


%prep
%autosetup -p 1 -n node-gdal-%{version}-fedora
sed -i -e 's/python /python3 /g' common.gypi
%nodejs_fixdep --remove node-pre-gyp
%nodejs_fixdep --dev --move nan "^2.1.0"
rm -rf deps node_modules


%build
%nodejs_symlink_deps --build
export CXXFLAGS="%{optflags}"
export LDFLAGS="%{?__global_ldflags} -Wl,-z,undefs"
node-gyp configure -- -Dshared_gdal=true -Dmodule_name=gdal -Dmodule_path=lib/binding
node-gyp build


%install
mkdir -p %{buildroot}%{nodejs_sitearch}/gdal
cp -pr package.json lib %{buildroot}%{nodejs_sitearch}/gdal
chmod 755 %{buildroot}%{nodejs_sitearch}/gdal/lib/binding/gdal.node
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%ifnarch s390x
%{nodejs_sitelib}/mocha/bin/mocha test -R tap --timeout 600000 --no-colors -gc --require ./test/_common.js
%endif


%files
%doc README.md AUTHORS CHANGELOG examples
%license LICENSE
%{nodejs_sitearch}/gdal


%changelog
* Thu May 21 2020 Sandro Mani <manisandro@gmail.com> - 0.9.9-4
- Rebuild (gdal)

* Tue Mar 03 2020 Sandro Mani <manisandro@gmail.com> - 0.9.9-3
- Rebuild (gdal)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 16 2019 Tom Hughes <tom@compton.nu> - 0.9.9-1
- Update to 0.9.9 upstream release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 14 2019 Tom Hughes <tom@compton.nu> - 0.9.8-3
- Rebuild for Node.js 12.4.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 31 2019 Tom Hughes <tom@compton.nu> - 0.9.8-1
- Update to 0.9.8 upstream release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Tom Hughes <tom@compton.nu> - 0.9.7-1
- Update to 0.9.7 upstream release

* Fri Jun 22 2018 Tom Hughes <tom@compton.nu> - 0.9.6-6
- Rebuild for Node.js 10.5.0

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Tom Hughes <tom@compton.nu> - 0.9.6-4
- Allow undefined symbols in the shared object
- Patch gdal 2.2.x issues in tests

* Wed Oct  4 2017 Tom Hughes <tom@compton.nu> - 0.9.6-3
- Re-enable tests

* Wed Oct 04 2017 Jared Smith <jsmith@fedoraproject.org> - 0.9.6-2
- Rebuild for gdal 2.2.x
- Disable tests due to segfault in tests

* Sun Aug 20 2017 Tom Hughes <tom@compton.nu> - 0.9.6-1
- Update to 0.9.6 upstream release

* Fri Aug 18 2017 Tom Hughes <tom@compton.nu> - 0.9.5-1
- Update to 0.9.5 upstream release

* Thu Aug 10 2017 Tom Hughes <tom@compton.nu> - 0.9.4-5.1
- Rebuild for Node.js 8.3.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-4.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 28 2017 Tom Hughes <tom@compton.nu> - 0.9.4-2.1
- Rebuild for Node.js 8.1.2

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 30 2016 Tom Hughes <tom@compton.nu> - 0.9.4-1
- Update to 0.9.4 upstream release

* Tue Sep 13 2016 Tom Hughes <tom@compton.nu> - 0.9.3-2
- Rebuild for Node.js 6.5.0

* Fri Sep  9 2016 Tom Hughes <tom@compton.nu> - 0.9.3-1.1
- Update to 0.9.3 upstream release

* Mon Aug 29 2016 Tom Hughes <tom@compton.nu> - 0.9.2-2.1
- Rebuild for Node.js 6.5.0

* Mon May 09 2016 Stephen Gallagher <sgallagh@redhat.com> - 0.9.2-1.1
- Rebuild for Node.js 6.1.0 upgrade

* Fri May  6 2016 Tom Hughes <tom@compton.nu> - 0.9.2-1
- Update to 0.9.2 upstream release

* Sun Apr 10 2016 Tom Hughes <tom@compton.nu> - 0.9.1-1
- Update to 0.9.1 upstream release

* Tue Mar 29 2016 Tom Hughes <tom@compton.nu> - 0.9.0-1
- Update to 0.9.0 upstream release

* Wed Mar 23 2016 Tom Hughes <tom@compton.nu> - 0.8.0-7
- Rebuild for Node.js 4.4.x

* Wed Feb 10 2016 Tom Hughes <tom@compton.nu> - 0.8.0-6
- Rebuild for Node.js 4.3.x

* Sat Feb  6 2016 Tom Hughes <tom@compton.nu> - 0.8.0-5
- Enable tests that require GEOS support

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec  4 2015 Tom Hughes <tom@compton.nu> - 0.8.0-3
- Rebuild for nodejs 4.2.3

* Wed Dec  2 2015 Tom Hughes <tom@compton.nu> - 0.8.0-2
- Rebuild for nodejs 4.2

* Mon Nov 23 2015 Tom Hughes <tom@compton.nu> - 0.8.0-1
- Initial build of 0.8.0

# The unit tests aren't in the npm release anymore, and upstream doesn't tag releases,
# so... we have to do this.
%global commit0 81b68829b2687fff3297b3115910898010ed6dd2
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%global npmname qtdatastream

Name:           nodejs-%{npmname}
Version:        1.1.0
Release:        3%{?dist}
Summary:        Nodejs lib which can read/write Qt formatted Datastreams

License:        MIT
URL:            https://www.npmjs.com/package/%{npmname}

Source0:        https://github.com/magne4000/node-qtdatastream/archive/%{commit0}/%{npmname}-%{shortcommit0}.tar.gz

BuildRequires:  nodejs-packaging

BuildRequires:  nodejs-debug, nodejs-int64-buffer

BuildRequires:  nodejs-grunt, nodejs-grunt-contrib-nodeunit
BuildRequires:  nodejs-grunt-cli

BuildArch:      noarch
ExclusiveArch: %{nodejs_arches} noarch

%description
Nodejs lib which can read/write Qt formatted Datastreams.

For the moment the following types are handled for reading and writing:
QBool, QShort, QInt, QInt64, QUInt, QUInt64, QDouble, QMap, QList, QString,
QVariant, QStringList, QByteArray, QUserType, QDateTime, QTime, QChar,
QInvalid.

%prep
%autosetup -n node-%{npmname}-%{commit0}

# Do not load nodejs-grunt-jsdoc for now.
# or grunt-eslint.
sed "s,grunt.loadNpmTasks('grunt-jsdoc');,//grunt.loadNpmTasks('grunt-jsdoc');," -i Gruntfile.js
sed "s,grunt.loadNpmTasks('grunt-eslint');,//grunt.loadNpmTasks('grunt-eslint');," -i Gruntfile.js

# Remove hidden .jshintrc file
#rm lib/.jshintrc

# Remove test which requires babel. (fix one day?)
rm test/decorators_test.js

# Fix dependencies.
%nodejs_fixdep debug

%build
# Nothing to build, this is a noarch package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npmname}
cp -a index.js src/ %{buildroot}%{nodejs_sitelib}/%{npmname}/
cp -a package.json %{buildroot}%{nodejs_sitelib}/%{npmname}/

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'

# Run nodeunit tests.
grunt nodeunit --force

%files
%{nodejs_sitelib}/%{npmname}/
%license LICENSE-MIT
%doc README.md

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 23 2019 Ben Rosser <rosser.bjr@gmail.com> - 1.1.0-1
- Updated to latest upstream release, 1.1.0 (rhbz#1668384).

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon May 21 2018 Ben Rosser <rosser.bjr@gmail.com> - 1.0.2-1
- Updated to latest upstream release (rhbz#1564474).

* Tue Mar 06 2018 Ben Rosser <rosser.bjr@gmail.com> - 1.0.1-1
- Updated to latest upstream release (#1551562).

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 11 2017 Ben Rosser <rosser.bjr@gmail.com> - 1.0.0-2
- Add missing index.js file to package.

* Tue Jun 20 2017 Ben Rosser <rosser.bjr@gmail.com> - 1.0.0-1
- Updated to latest upstream release.

* Sun Feb 26 2017 Ben Rosser <rosser.bjr@gmail.com> - 0.7.1-1
- Updated to latest upstream release.

* Wed Feb 08 2017 Ben Rosser <rosser.bjr@gmail.com> - 0.7.0-1
- Updated to latest upstream release.

* Sun Jan 01 2017 Ben Rosser <rosser.bjr@gmail.com> - 0.6.7-2
- Remove hidden .jshintrc file from package.

* Tue Nov 22 2016 Ben Rosser <rosser.bjr@gmail.com> - 0.6.7-1
- Update to latest upstream release, fixing another date conversion bug.

* Wed Jun 29 2016 Ben Rosser <rosser.bjr@gmail.com> - 0.6.6-1
- Update to latest upstream release, fixing a bug with the unit tests.

* Wed Jun 29 2016 Ben Rosser <rosser.bjr@gmail.com> - 0.6.5-1
- Initial package.

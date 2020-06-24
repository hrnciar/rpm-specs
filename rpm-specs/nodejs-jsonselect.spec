%{?nodejs_find_provides_and_requires}

%global packagename JSONSelect
%global enable_tests 1

Name:		nodejs-jsonselect
Version:	0.4.0
Release:	14%{?dist}
Summary:	CSS-like selectors for JSON

License:	ISC
URL:		https://github.com/lloyd/JSONSelect.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
Source1:	https://raw.githubusercontent.com/lloyd/JSONSelect/master/LICENSE

Patch0:		nodejs-jsonselect_fix-print.patch

BuildArch:	noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:	nodejs-packaging
%if 0%{?enable_tests}
BuildRequires:	uglify-js
%endif

%description
CSS-like selectors for JSON


%prep
%setup -q -n package
%patch0 -p1
cp -p %{SOURCE1} .

# rename the build directory, so that we can delete most of it
# since in bundles js-hint and uglify-js
mv src/build src/build.disabled
# make a new (clean) build directory
mkdir src/build
# copy over only the script that is needed
cp src/build.disabled/post-compile.js src/build
# remove the bundled files and the dist directory
rm -rf src/build.disabled src/dist
# make a new clean dist directory
mkdir src/dist
# also remove the "site" directory, as it contains a bunch of bundled libs
rm -rf site



%build
pushd src
# I know this seems silly, as the makefile just copies the file from
# src/ to src/dist/, but it might do more in the future
make project
# Manually minify and post-process the file, as the Makefile is hardcoded to
# the bundled version of uglify-js
%{_bindir}/uglifyjs dist/jsonselect.js > dist/jsonselect.min.js.tmp
%__nodejs build/post-compile.js dist/jsonselect.min.js.tmp > dist/jsonselect.min.js
popd
# Now create a new "src" directory with only the built results, and without all the tests
mv src src.complete
mkdir src
cp src.complete/dist/*.js src/

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json src/ \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
%__nodejs src.complete/test/run.js
%endif


%files
%{!?_licensedir:%global license %doc}
%doc *.md
%license LICENSE
%{nodejs_sitelib}/%{packagename}



%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 11 2019 Jared K. Smith <jsmith@fedoraproject.org> - 0.4.0-13
- Fix removal of sys.print in NodeJS

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 25 2015 Jared Smith <jsmith@fedoraproject.org> - 0.4.0-5
- Rename package to all lower case

* Tue Nov 24 2015 Jared Smith <jsmith@fedoraproject.org> - 0.4.0-4
- Add missing BuildRequires for uglify-js

* Tue Nov 24 2015 Jared Smith <jsmith@fedoraproject.org> - 0.4.0-2
- Remove errant BuildRequire

* Tue Nov 24 2015 Jared Smith <jsmith@fedoraproject.org> - 0.4.0-1
- Initial packaging

# This macro is needed at the start for building on EL6
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

%global barename es5-shim

Name:               nodejs-es5-shim
Version:            4.1.0
Release:            10%{?dist}
Summary:            ECMAScript 5 compatibility shims for legacy JavaScript engines

License:            MIT
URL:                https://www.npmjs.org/package/es5-shim
Source0:            http://registry.npmjs.org/%{barename}/-/%{barename}-%{version}.tgz
BuildArch:          noarch
%if 0%{?fedora} >= 19
ExclusiveArch:      %{nodejs_arches} noarch
%else
ExclusiveArch:      %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:      nodejs-packaging >= 6
BuildRequires:      npm(uglify-js)

%if 0%{?enable_tests}
BuildRequires:      npm(jscs)
BuildRequires:      npm(jasmine-node)
%endif

%description
es5-shim.js and es5-shim.min.js monkey-patch a JavaScript context to contain
all EcmaScript 5 methods that can be faithfully emulated with a legacy
JavaScript engine.

es5-sham.js and es5-sham.min.js monkey-patch other ES5 methods as closely as
possible. For these methods, as closely as possible to ES5 is not very close.
Many of these shams are intended only to allow code to be written to ES5
without causing run-time errors in older engines. In many cases, this means
that these shams cause many ES5 methods to silently fail. Decide carefully
whether this is what you want. Note: es5-sham.js requires es5-shim.js to be
able to work properly.

%prep
%setup -q -n package

# Remove bundled node_modules if there are any..
rm -rf node_modules/

%nodejs_fixdep --caret

%build
%nodejs_symlink_deps --build

uglifyjs es5-shim.js --comments --source-map=es5-shim.map -m -b ascii_only=true,beautify=false > es5-shim.min.js
uglifyjs es5-sham.js --comments --source-map=es5-sham.map -m -b ascii_only=true,beautify=false > es5-sham.min.js


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/es5-shim
cp -pr package.json es5-shim.js es5-sham.min.js es5-sham.js es5-shim.min.js \
    %{buildroot}%{nodejs_sitelib}/es5-shim

%nodejs_symlink_deps

%check
%if 0%{?enable_tests}
%nodejs_symlink_deps --check
npm run lint && jasmine-node --matchall ./ tests/spec/
%endif

%files
%doc LICENSE README.md
%{nodejs_sitelib}/es5-shim/

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 18 2015 Ralph Bean <rbean@redhat.com> - 4.1.0-1
- new version

* Mon Sep 15 2014 Ralph Bean <rbean@redhat.com> - 4.0.3-2
- Run minify/uglify step in the build section as per review request.
- Added BR on uglify-js.

* Mon Sep 15 2014 Ralph Bean <rbean@redhat.com> - 4.0.3-1
- Initial packaging for Fedora.

%{?nodejs_find_provides_and_requires}

#enable/disable tests in case the deps aren't there
%global enable_tests 0

Name:           uglify-js1
Version:        1.3.4
Release:        19%{?dist}
Summary:        JavaScript parser, mangler/compressor and beautifier toolkit

# BSD license in README.html
License:        BSD
URL:            https://github.com/mishoo/UglifyJS
Source0:        http://registry.npmjs.org/uglify-js/-/uglify-js-%{version}.tgz

BuildArch:      noarch
%if 0%{?fedora} >= 19 || 0%{?rhel} > 7
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  nodejs-packaging
BuildRequires:  web-assets-devel

%if 0%{?enable_tests}
BuildRequires:  npm(nodeunit)
%endif

Requires: js-uglify-1 = %{version}-%{release}

%description
JavaScript parser, mangler/compressor and beautifier toolkit.  This is the
classic 1.x version of uglify-js.  Consider using the new version provided
in the uglify-js package.

This package ships the uglifyjs command-line tool and a library suitable for
use within Node.js.

%package -n js-uglify-1
Summary: JavaScript parser, mangler/compressor and beautifier toolkit - core library


Obsoletes: uglify-js1-common < 1.3.4-4
Provides: uglify-js1-common = %{version}-%{release}
Requires: web-assets-filesystem

%description -n js-uglify-1
JavaScript parser, mangler/compressor and beautifier toolkit.  This is the
classic 1.x version of uglify-js.  Consider using the new version provided
in the uglify-js package.

This package ships a JavaScript library suitable for use by any JavaScript
runtime.


%prep
%setup -q -n package


%build
#nothing to do


%install
rm -rf %buildroot


mkdir -p %{buildroot}%{_jsdir}/uglify-js-1
cp -pr lib/* %{buildroot}%{_jsdir}/uglify-js-1

#compat symlink
mkdir -p %{buildroot}%{_datadir}
ln -sf javascript/uglify-js-1 %{buildroot}%{_datadir}/%{name}

mkdir -p %{buildroot}%{nodejs_sitelib}/uglify-js@1
cp -pr bin package.json uglify-js.js %{buildroot}%{nodejs_sitelib}/uglify-js@1
ln -sf %{_jsdir}/uglify-js-1 %{buildroot}%{nodejs_sitelib}/uglify-js@1/lib

##compat symlink so old modules continue to work
ln -sf uglify-js@1 %{buildroot}%{nodejs_sitelib}/%{name}

mkdir -p %{buildroot}%{_bindir}
ln -sf ../lib/node_modules/uglify-js1/bin/uglifyjs %{buildroot}%{_bindir}/uglifyjs1

#nodejs-symlink-deps is not called because this package does not have any
#dependencies and can be used outside of node


%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
nodeunit test/unit/scripts.js && test/testparser.js && test/testconsolidator.js
%endif



%pretrans -p <lua>
st = posix.stat("%{nodejs_sitelib}/uglify-js1")
if st and st.type == "directory" then
  os.execute("rm -rf %{nodejs_sitelib}/uglify-js1")
end

%pretrans -n js-uglify-1 -p <lua>
st = posix.stat("%{_datadir}/%{name}")
if st and st.type == "directory" then
  os.execute("rm -rf %{_datadir}/%{name}")
end


%files
%{nodejs_sitelib}/uglify-js@1
%{nodejs_sitelib}/uglify-js1
%{_bindir}/uglifyjs1

%files -n js-uglify-1
%{_jsdir}/uglify-js-1
%{_datadir}/%{name}
%doc README.html README.org docstyle.css

%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 05 2017 Troy Dawson <tdawson@redhat.com> - 1.3.4-14
- Minor spec file cleanup

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 29 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.3.4-9
- add logic for building on EL6

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 10 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.3.4-7
- fix scriptlets to run in the correct subpackages

* Mon Jan 20 2014 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.3.4-6
- fix Requires on js-uglify-1 subpackage

* Mon Jan 20 2014 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.3.4-5
- port to new JS guidelines

* Mon Jan 20 2014 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.3.4-4
- add compat symlink so old modules continue to work

* Sun Jan 19 2014 Tom Hughes <tom@compton.nu> - 1.3.4-3
- use new multi-version packaging rules
- update to latest nodejs packaging standards

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 01 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.3.4
- initial package based on the uglify-js (2.x) pacakge

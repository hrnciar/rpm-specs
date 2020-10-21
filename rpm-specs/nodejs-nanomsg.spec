%global npm_name nanomsg
%global debug_package %{nil}

%{?nodejs_find_provides_and_requires}

Name:           nodejs-%{npm_name}
Version:        4.1.0
Release:        4%{?dist}
Summary:        nanomsg for node
License:        MIT
URL:            https://github.com/nickdesaulniers/node-nanomsg
Source0:        https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
ExclusiveArch:  %{nodejs_arches}

BuildRequires:  nodejs-devel
BuildRequires:  node-gyp
BuildRequires:  npm(nan)
BuildRequires:  npm(bindings)
#For tests
BuildRequires:  npm(tape)

%description
Node.js binding for nanomsg

%prep
%setup -q -n package
%nodejs_fixdep bindings ">=1.2.1"
%nodejs_fixdep nan ">=2.8"

%build
%nodejs_symlink_deps --build
%set_build_flags
node-gyp configure
node-gyp build

%install
mkdir -p %{buildroot}/%{nodejs_sitearch}/nanomsg
cp -pr build lib package.json perf %{buildroot}/%{nodejs_sitearch}/nanomsg
%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
#Cleanup bad tests for the enviroment
rm -f test/{send,sockoptapi,transform,ws}.js
find test/*.js test/standalone/*.js | xargs -n 1 node
echo "Finished tests"
 
%files
%doc README.md examples
%license LICENSE
%{nodejs_sitearch}/%{npm_name}

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 16 2019 Troy Dawson <tdawson@redhat.com> - 4.1.0-1
- Update to 4.1.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jan 29 2019 Troy Dawson <tdawson@redhat.com> - 4.0.2-2
- Update what get's copied over in the install phase

* Wed Dec 19 2018 Troy Dawson <tdawson@redhat.com> - 4.0.2-1
- Initial build

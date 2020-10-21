# Generated from hiera-vault-0.2.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name hiera-vault

Name: rubygem-%{gem_name}
Version: 0.2.2
Release: 9%{?dist}
Summary: Module for using vault as a hiera backend
License: ASL 2.0
URL: http://github.com/jsok/hiera-vault
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# Fix translation isue with version 5 hiera.yaml
# https://github.com/jsok/hiera-vault/pull/34
Patch0: hiera-vault-34.patch

# Vault kv2 - based on upstream PR, with default field fixes
# https://github.com/jsok/hiera-vault/pull/37
Patch1: hiera-vault-37.patch

BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildArch: noarch

%description
Hiera backend for looking up secrets stored in Vault.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%patch0 -p1
%patch1 -p1

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/



%check
pushd .%{gem_instdir}
# Run the test suite.
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar  2 2020 Ed Marshall <esm@logic.net> - 0.2.2-8
- Add initial support for kv v2.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 13 2017 Ed Marshall <esm@logic.net> - 0.2.2-2
- Add patch to fix issue with v5 hiera configuration.

* Thu Oct 26 2017 mockbuilder - 0.2.2-1
- Initial package

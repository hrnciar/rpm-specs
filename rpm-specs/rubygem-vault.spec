# Generated from vault-0.12.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name vault

# Filter out the automatic addition of requires on aws-sigv4, since it's
# explicitly optional, and not currently packaged for Fedora.
%global __requires_exclude ^rubygem\\(aws-sigv4\\)

Name: rubygem-%{gem_name}
Version: 0.13.1
Release: 2%{?dist}
Summary: A Ruby API client for interacting with a Vault server
License: MPLv2.0
URL: https://github.com/hashicorp/vault-ruby
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
# BuildRequires: rubygem(pry) >= 0.13.1
# BuildRequires: rubygem(pry) < 0.14
# BuildRequires: rubygem(rspec) >= 3.5
# BuildRequires: rubygem(rspec) < 4
# BuildRequires: rubygem(yard) >= 0.9.24
# BuildRequires: rubygem(yard) < 0.10
# BuildRequires: rubygem(webmock) >= 3.8.3
# BuildRequires: rubygem(webmock) < 3.9
BuildArch: noarch

%description
%{summary}


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/



%check
pushd .%{gem_instdir}
# rspec spec
popd

%files
%dir %{gem_instdir}
%{gem_instdir}/.circleci
%exclude %{gem_instdir}/.gitignore
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%exclude %{gem_instdir}/.rspec
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/vault.gemspec

%changelog
* Sun May 03 2020 Ed Marshall <esm@logic.net> - 0.13.1-2
- Filter out aws-sigv4 requirement, since it's explicitly optional.

* Fri May 01 2020 Ed Marshall <esm@logic.net> - 0.13.1-1
- Update to 0.13.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 01 2019 Ed Marshall <esm@logic.net> - 0.13.0-1
- Update to 0.13.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 08 2018 Ed Marshall <esm@logic.net> - 0.12.0-1
- Update to 0.12.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Oct 25 2017 Ed Marshall <esm@logic.net> - 0.10.1-1
- Initial package

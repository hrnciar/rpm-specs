# Generated from public_suffix-2.0.5.gem by gem2rpm -*- rpm-spec -*-
%global gem_name public_suffix

Name: rubygem-%{gem_name}
Version: 4.0.5
Release: 1%{?dist}
Summary: Domain name parser based on the Public Suffix List
# MPLv2.0: %%{gem_instdir}/data/list.txt
License: MIT and MPLv2.0
URL: https://simonecarletti.com/code/publicsuffix-ruby
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(mocha)
BuildArch: noarch

%description
PublicSuffix can parse and decompose a domain name into top level domain,
domain and subdomains.


%package doc
Summary: Documentation for %{name}
# Public Domain: %%{gem_instdir}/test/tests.txt
License: MIT and Public Domain
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n  %{gem_name}-%{version}

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
# We don't have minitest-reporters in Fedora yet, but they are not needed
# very likely.
sed -i '/[Rr]eporters/ s/^/#/' test/test_helper.rb

LANG=C.utf-8 ruby -Itest -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/LICENSE.txt
# This is usefull just for development.
%exclude %{gem_instdir}/bin
%{gem_instdir}/data
%{gem_libdir}
%exclude %{gem_instdir}/public_suffix.gemspec
%exclude %{gem_cache}
%{gem_spec}
%exclude %{gem_instdir}/test/.empty
%exclude %{gem_instdir}/codecov.yml

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/2.0-Upgrade.md
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/SECURITY.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%changelog
* Fri Jun 05 2020 Pavel Valena <pvalena@redhat.com> - 4.0.5-1
- Update to public_suffix 4.0.5.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 13 2017 Vít Ondruch <vondruch@redhat.com> - 3.0.1-1
- Update to PublicSuffix 3.0.1.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Apr 07 2017 Vít Ondruch <vondruch@redhat.com> - 2.0.5-2
- Fix license fields.

* Thu Apr 06 2017 Vít Ondruch <vondruch@redhat.com> - 2.0.5-1
- Initial package

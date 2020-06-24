# Generated from hiredis-0.6.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name hiredis

Name: rubygem-%{gem_name}
Version: 0.6.3
Release: 3%{?dist}
Summary: Ruby wrapper for hiredis
License: BSD
URL: http://github.com/redis/hiredis-rb
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Get the test suite:
# git clone https://github.com/redis/hiredis-rb.git && cd hiredis-rb/
# git checkout v0.6.3 && tar czvf hiredis-0.6.3-tests.tgz test/
Source1: %{gem_name}-%{version}-tests.tgz
# Build against system hiredis library
Patch0: rubygem-hiredis-0.6.1-Build-against-system-hiredis.patch
# Compatibility with older hiredis we have in Fedora
# Revert: https://github.com/redis/hiredis-rb/pull/53
# https://github.com/redis/hiredis-rb/commit/5284a0403bca7fbd9a086f9d8501a053a65beb67
Patch1: rubygem-hiredis-0.6.3-Support-older-hiredis-version.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby-devel
BuildRequires: gcc
BuildRequires: hiredis-devel
BuildRequires: rubygem(minitest)

%description
Ruby wrapper for hiredis (protocol serialization/deserialization and blocking
I/O).

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version} -b1


# Remove bundled hiredis
%gemspec_remove_file Dir.glob('vendor/**/*')
rm -rf ./vendor

# Use system hiredis
%patch0 -p1
%patch1 -p1


%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{gem_extdir_mri}/hiredis/ext
cp -a .%{gem_extdir_mri}/gem.build_complete %{buildroot}%{gem_extdir_mri}/
cp -a .%{gem_extdir_mri}/%{gem_name}/ext/*.so %{buildroot}%{gem_extdir_mri}/%{gem_name}/ext

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/


%check
pushd .%{gem_instdir}
# Unpack the test suite
tar xzf %{SOURCE1}

# The connection does not recover, probably hiredis version mismatch
# https://github.com/redis/hiredis-rb/issues/62
sed -i '/^  def test_recover_from_partial_write/ a skip' \
  test/connection_test.rb

ruby -Ilib:$(dirs +1)%{gem_extdir_mri} -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%{gem_extdir_mri}
%license %{gem_instdir}/COPYING
%{gem_libdir}
%exclude %{gem_cache}
%exclude %{gem_instdir}/ext
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Rakefile

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 16 2020 Pavel Valena <pvalena@redhat.com> - 0.6.3-2
- Rebuild for Ruby 2.7: https://fedoraproject.org/wiki/Changes/Ruby_2.7

* Mon Sep 30 2019 Pavel Valena <pvalena@redhat.com> - 0.6.3-1
- Update to hiredis 0.6.3.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 17 2019 Vít Ondruch <vondruch@redhat.com> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.6

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 01 2018 Pavel Valena <pvalena@redhat.com> - 0.6.1-1
- Initial package

# Generated from bootsnap-1.3.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name bootsnap

Name: rubygem-%{gem_name}
Version: 1.3.2
Release: 5%{?dist}
Summary: Boot large ruby/rails apps faster
License: MIT
URL: https://github.com/Shopify/bootsnap
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# The bootsnap gem doesn't ship with the test suite.
# You may check it out like so:
# git clone http://github.com/Shopify/bootsnap.git && cd bootsnap
# git checkout v1.3.2 && tar czvf bootsnap-1.3.2-tests.tgz test/
Source1: %{gem_name}-%{version}-tests.tgz
# https://github.com/Shopify/bootsnap/commit/a163c7cddfccd68277f6ea43b1831378509817c9
Patch1:  rubygem-bootsnap-ruby27.patch

BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby-devel >= 2.0.0
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(mocha)
# Bundler is needed just for one test, that is failing atm.
# BuildRequires: rubygem(bundler)
BuildRequires: rubygem(msgpack)
# Compiler is required for build of gem binary extension.
# https://fedoraproject.org/wiki/Packaging:C_and_C++#BuildRequires_and_Requires
BuildRequires: gcc

# Tests crash on armv7hl. Upstream issues:
# https://github.com/Shopify/bootsnap/issues/67
# https://bugs.ruby-lang.org/issues/13670
ExcludeArch: armv7hl

# Note - rpmlint shows error:
# call-to-mktemp /usr/lib64/gems/ruby/bootsnap-1.3.0/bootsnap/bootsnap.so
# https://github.com/Shopify/bootsnap/issues/174

%description
Bootsnap is a library that plugs into Ruby, with optional support
for ActiveSupport and YAML, to optimize and cache expensive computations.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version} -a 1
%patch1 -p1

sed -i -e "/^\s*\$CFLAGS / s/^/#/g" \
  ext/bootsnap/extconf.rb

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{gem_extdir_mri}/%{gem_name}
cp -a .%{gem_extdir_mri}/gem.build_complete %{buildroot}%{gem_extdir_mri}/
cp -a .%{gem_extdir_mri}/%{gem_name}/*.so %{buildroot}%{gem_extdir_mri}/%{gem_name}

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/

%check
# copy the previously unpacked test files
cp -a test/ .%{gem_instdir}
pushd .%{gem_instdir}

# Remove bundler dependency, also, we have
# newer minitest than upstream is testing with.
sed -i -e "/require 'bundler/ s/^/#/g" \
       -e "/require 'mocha\/minitest/ s/minitest/mini_test/g" \
  test/test_helper.rb

# '/usr/share/ruby/time.rb' is expected to be in stable prefix,
# but that is failing for some reason. Same issue with bundler.
# https://github.com/Shopify/bootsnap/issues/173
sed -i -e "/^\s*assert stable.stable?,/ s/^/#/g" \
       -e "/^\s*refute stable.volatile?,/ s/^/#/g" \
       -e "/^\s*assert bundler.stable?,/ s/^/#/g" \
       -e "/^\s*Bundler/ s/^/#/g" \
  test/load_path_cache/path_test.rb

ruby -Ilib:test:ext -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd


%files
%dir %{gem_instdir}
%{gem_extdir_mri}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/LICENSE.txt
%exclude %{gem_instdir}/bootsnap.gemspec
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTING.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.jp.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/dev.yml
%{gem_instdir}/shipit.rubygems.yml
%{gem_instdir}/bin
%doc %{gem_instdir}/CODE_OF_CONDUCT.md

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 20 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.3.2-4
- Apply upstream patch to support ruby 2.7
- Unpack test tarball beforehand, as the above patch needs applying
- Rebuild against ruby27

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 18 2019 Pavel Valena <pvalena@redhat.com> - 1.3.2-1
- Update to Bootsnap 1.3.2.
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.6

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 30 2018 Pavel Valena <pvalena@redhat.com> - 1.3.0-1
- Initial package

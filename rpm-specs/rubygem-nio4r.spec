# Generated from nio4r-1.2.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name nio4r

%global libev_version 4.27

Name: rubygem-%{gem_name}
Version: 2.5.2
Release: 3%{?dist}
Summary: New IO for Ruby
# The entire source code is MIT, bundled libev is BSD or GPLv2+
License: MIT and (BSD or GPLv2+)
URL: https://github.com/socketry/nio4r
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby-devel
BuildRequires: rubygem(rspec)
# Compiler is required for build of gem binary extension.
# https://fedoraproject.org/wiki/Packaging:C_and_C++#BuildRequires_and_Requires
BuildRequires: gcc

# As bundled libev ev.c is modified from original one,
# we have to use the bundled libev instead of separating it and
# using system libev.
# See below commits.
# Release the GIL when libev polls
# https://github.com/socketry/nio4r/commit/6801433
# A more productive message re: GVL
# https://github.com/socketry/nio4r/commit/fba5c68
Provides: bundled(libev) = %{libev_version}

%description
Cross-platform asynchronous I/O primitives for scalable network clients and
servers. Inspired by the Java NIO API, but simplified for ease-of-use.


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

# Update %%optflags used in %%gem_install to avoid strict-aliasing warnings.
# https://github.com/socketry/nio4r/pull/130
# http://pkgs.fedoraproject.org/cgit/rpms/rubygems.git/tree/macros.rubygems
%global optflags %{?optflags} -fno-strict-aliasing

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/{gem.build_complete,*.so} %{buildroot}%{gem_extdir_mri}/

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/


%check
pushd .%{gem_instdir}
# Check libev version correctness.
EV_VERSION_MAJOR=$(grep EV_VERSION_MAJOR ext/libev/ev.h | cut -d ' ' -f3)
EV_VERSION_MINOR=$(grep EV_VERSION_MINOR ext/libev/ev.h | cut -d ' ' -f3)
[ "${EV_VERSION_MAJOR}.${EV_VERSION_MINOR}" = '%{libev_version}' ]

# Ignore code coverage and bundler.
sed -i '/require "coveralls"/ s/^/#/' spec/spec_helper.rb
sed -i '/Coveralls.wear!/ s/^/#/' spec/spec_helper.rb

# Load nio4r_ext.so.
rspec -I$(dirs +1)%{gem_extdir_mri} spec
popd

%files
%dir %{gem_instdir}
%{gem_extdir_mri}
%exclude %{gem_instdir}/.*
# License file was removed in favor of README.md
# https://github.com/socketry/nio4r/issues/228
%license %{gem_instdir}/README.md
%exclude %{gem_instdir}/appveyor.yml
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/CHANGES.md
%{gem_instdir}/logo.png
%{gem_instdir}/rakelib
%{gem_instdir}/Guardfile
%{gem_instdir}/Rakefile
%{gem_instdir}/examples
%{gem_instdir}/nio4r.gemspec
%{gem_instdir}/spec

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Pavel Valena <pvalena@redhat.com> - 2.5.2-1
- Update to nio4r 2.5.2.

* Fri Jan 17 2020 Vít Ondruch <vondruch@redhat.com> - 2.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.7

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 09 2019 Vít Ondruch <vondruch@redhat.com> - 2.4.0-1
- Update to nio4r 2.4.0.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 28 2019 Vít Ondruch <vondruch@redhat.com> - 2.3.1-3
- Temporary disable test failing due to OpenSSL 1.1.1.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 11 2018 Jun Aruga <jaruga@redhat.com> - 2.3.1-1
- Update to nio4r 2.3.1.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 2.2.0-3
- Rebuilt for switch to libxcrypt

* Thu Jan 04 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.2.0-2
- F-28: rebuild for ruby25

* Thu Jan 04 2018 Vít Ondruch <vondruch@redhat.com> - 2.2.0-1
- Update to nio4r 2.2.0.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 31 2017 Jun Aruga <jaruga@redhat.com> - 2.1.0-2
- Add check of libev version correctness.

* Mon May 29 2017 Jun Aruga <jaruga@redhat.com> - 2.1.0-1
- Update to nio4r 2.1.0.

* Wed Mar 22 2017 Jun Aruga <jaruga@redhat.com> - 2.0.0-1
- Update to nio4r 2.0.0.

* Tue Feb 21 2017 Jun Aruga <jaruga@redhat.com> - 1.2.1-5
- Add flag to avoid warnings from strict-aliasing optimization.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Vít Ondruch <vondruch@redhat.com> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.4

* Thu Jun 30 2016 Jun Aruga <jaruga@redhat.com> - 1.2.1-2
- Swap the description and summary

* Tue Jun 28 2016 Jun Aruga <jaruga@redhat.com> - 1.2.1-1
- Initial package

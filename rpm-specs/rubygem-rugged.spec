%global gem_name rugged

Summary:       Rugged is a Ruby binding to the libgit2 library
Name:          rubygem-%{gem_name}
Version:       1.0.0
Release:       1%{?dist}
License:       MIT
URL:           https://github.com/libgit2/rugged
Source0:       https://rubygems.org/gems/%{gem_name}-%{version}.gem
# The test directory for this version is incomplete due to gemspec bug.
# Upstream has removed test and Rakefile from gem in future versions.
# https://github.com/libgit2/rugged/issues/262
# https://github.com/libgit2/rugged/pull/263
# This is how we are getting the tests (Source1)
#  git clone https://github.com/libgit2/rugged
#  git -C rugged archive --format=tar.gz -o $PWD/rugged-1.0.0-test.tgz v1.0.0 -- Rakefile test/
Source1:       %{gem_name}-%{version}-test.tgz
Requires:      ruby(rubygems)
Requires:      ruby
BuildRequires:  gcc
BuildRequires: ruby
BuildRequires: git-core
BuildRequires: cmake
BuildRequires: libgit2-devel
BuildRequires: ruby-devel
BuildRequires: rubygem(minitest)
BuildRequires: rubygems-devel
Provides:      rubygem(%{gem_name}) = %{version}

%description
Rugged is a Ruby bindings to the libgit2W C Git library. This is
for testing and using the libgit2 library in a language that is awesome.


%package doc
Summary:       Documentation for %{name}
Requires:      %{name} = %{version}-%{release}
BuildArch:     noarch

%description doc
Documentation for %{name}.

%prep
%autosetup -n %{gem_name}-%{version} -a 1 -S git

rm -vrf vendor
# Remove the bundled libraries from gemspec
sed -i -e 's\, "vendor[^,]*"\\g' ../%{gem_name}-%{version}.gemspec

# The build system requres libgit2's version.h to be present, and defaults to
# using the vendor'd copy. Use the system copy instead.
sed -i -e 's|LIBGIT2_DIR = .*|LIBGIT2_DIR = "%{_prefix}"|' ext/rugged/extconf.rb

%build
export CONFIGURE_ARGS="--with-cflags='%{optflags}' --use-system-libraries"

gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/


# move C extensions to the extdir.
mkdir -p %{buildroot}%{gem_extdir_mri}/
cp -a .%{gem_extdir_mri}/{gem.build_complete,%{gem_name}/} %{buildroot}%{gem_extdir_mri}/

# We don't need those files anymore.
rm -rf %{buildroot}%{gem_instdir}/ext/

%check
#export LANG="C.UTF-8"
#git config --global user.name John Doe
# Comment out the test until we get the minitest/autorun figured out
# testrb -Ilib test/*test.rb

%files
%license %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.md
%dir %{gem_instdir}
%{gem_libdir}
%{gem_extdir_mri}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}

%changelog
* Wed Apr 15 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0

* Tue Mar 10 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.99.0-1
- Update to 0.99.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.28.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.28.0-4
- F-32: rebuild against ruby27

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.28.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 16 2019 Vít Ondruch <vondruch@redhat.com> - 0.28.0-2
- Remove useless %%{rubygems_default_filter} macro.

* Thu Jun 06 19:25:57 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.28.0-1
- Update to 0.28.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.27.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 17 2019 Vít Ondruch <vondruch@redhat.com> - 0.27.4-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.6

* Fri Aug 10 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.27.4-1
- Update to 0.27.4

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 0.26.0-9
- Rebuild with fixed binutils

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.26.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Feb 10 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.26.0-7
- Cleanups and fixes

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.26.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 0.26.0-5
- Rebuilt for switch to libxcrypt

* Thu Jan 04 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.26.0-4
- F-28: rebuild for ruby25

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.26.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.26.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 08 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.26.0-1
- Update to 0.26.0

* Tue Feb 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.25.1.1-1
- Update to 0.25.1.1 (RHBZ #1410965)

* Wed Jan 11 2017 Vít Ondruch <vondruch@redhat.com> - 0.24.6-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.4

* Tue Jan 10 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.24.6-1
- Update to 0.24.6

* Sun Mar 20 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.24.0-1
- Update to 0.24.0 (RHBZ #1314950)

* Thu Feb 18 2016 Jiri Popelka <jpopelka@redhat.com> - 0.23.3-1
- Update to version 0.23.3 (rhbz#1252642)
- Use %%license macro

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.23.0-0.20150733git233da19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 11 2016 Vít Ondruch <vondruch@redhat.com> - 0.23.0-0.20150732git233da19
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.3

* Fri Jul 31 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@Foobar.org> - 0.22.2-4.20150731git233da19
- Bump to latest git

* Fri Jul 31 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.22.2-3
- Rebuilt for libgit2-0.23.0 and libgit2-glib-0.23

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 25 2015 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.22.2-1
- Update to 0.22.2 (rhbz#1222540)
- Use HTTPS urls

* Tue May 05 2015 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.22.1-0.1.b1
- Update to version 0.22.1b1 (rhbz#1166414)

* Fri Jan 16 2015 Vít Ondruch <vondruch@redhat.com> - 0.21.0-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.2

* Fri Dec 26 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.21.0-3
- Install gem.build_complete on F-21 and move extension file to the
  correct location (bug 1176450)

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jul 03 2014 Troy Dawson <tdawson@redhat.com> - 0.21.0-1
- Update to version 0.21.0
- Comment out the test until we get minitest/autorun figured out

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Feb 05 2014 Troy Dawson <tdawson@redhat.com> - 0.19.0-6
- Misc packaging fixes (#1061552) Ken Dreyer

* Mon Jan 06 2014 Troy Dawson <tdawson@redhat.com> - 0.19.0-5
- Misc spec file fixes (#1048958) Ken Dreyer
- Change vendor patch to sed command

* Mon Sep 09 2013 Troy Dawson <tdawson@redhat.com> - 0.19.0-4
- Update comments about test source
- Fix zero length files in test

* Fri Sep 06 2013 Troy Dawson <tdawson@redhat.com> - 0.19.0-3
- Added full test directory
- use minitest for tests
- Added .so file provides filter

* Thu Aug 22 2013 Troy Dawson <tdawson@redhat.com> - 0.19.0-2
- remove vendor directory and patch gemspec to reflect that
- export LIBGIT2_PATH before building to use system git2

* Mon Jul 22 2013 Troy Dawson <tdawson@redhat.com> - 0.19.0-1
- Updated to latest release - 0.19.0
- Cleaned up bad tests
- Comment out check, due to bad exit code from successful tests

* Mon Jul 22 2013 Troy Dawson <tdawson@redhat.com> - 0.19.0-1
- Updated to latest release - 0.19.0
- Cleaned up bad tests

* Tue Jul 09 2013 Troy Dawson <tdawson@redhat.com> - 0.16.0-3
- Change build section to use current ruby guidelines
- move lib/rugged/rugged.so instead of ext/rugged/rugged.so
- move rugged.so into the correct directory
- cleanup test, now runs without problems

* Tue Jul 02 2013 Troy Dawson <tdawson@redhat.com> - 0.16.0-2
- Make macro's more consistant
- Remove extra rugged.so
- Set correct permissions for rugged.so
- Run test (thanks to Axilleas Pipinellis for this)
- Add libgit2-devel to buildrequires - this causes the build to
  use system libgit2 instead of bundled version.

* Mon Mar 18 2013 Troy Dawson <tdawson@redhat.com> - 0.16.0-1
- Initial package

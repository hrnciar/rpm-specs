%global gem_name thin

Name: rubygem-%{gem_name}
Version: 1.7.2
Release: 14%{?dist}
Summary: A thin and fast web server
# lib/thin/stats.html.erb: BSD
# spec/rails_app/public/javascripts/*.js: MIT
License: (GPLv2+ or Ruby) and BSD and MIT
URL: http://code.macournoyer.com/thin/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/macournoyer/thin.git && cd thing
# git checkout v1.7.2 && tar czvf thin-1.7.2-tests.tgz spec/
Source1: %{gem_name}-%{version}-tests.tgz
# Fix the test suite error due to way Ruby 2.5 reports warnings.
# https://github.com/macournoyer/thin/pull/346
Patch0: rubygem-thin-1.7.2-Mock-Kernel.warn-in-Ruby-2.5-compatible-way.patch
# Fix "Thin::Server should set lower maximum_connections size when too large"
# error caused probably by change of RLIMIT_NOFILE in Kernel or systemd.
# https://github.com/macournoyer/thin/pull/360
Patch1: rubygem-thin-1.7.2-Fix-maximum_connections-limiting-test.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby-devel
# Compiler is required for build of gem binary extension.
# https://fedoraproject.org/wiki/Packaging:C_and_C++#BuildRequires_and_Requires
BuildRequires: gcc
BuildRequires: rubygem(rspec2)
BuildRequires: rubygem(eventmachine) >= 1.0.4
BuildRequires: rubygem(daemons) >= 1.0.9
BuildRequires: rubygem(rack) >= 1.0.0

%description
Thin is a Ruby web server that glues together three of the best Ruby
libraries in web history.
The Mongrel parser, the root of Mongrel speed and security,
Event Machine, a network I/O library with extremely high scalability and
Rack, a minimal interface between webservers and Ruby frameworks.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version} -b 1

pushd %{_builddir}
%patch0 -p1
%patch1 -p1
popd

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

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/{gem.build_complete,*.so} %{buildroot}%{gem_extdir_mri}/

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/

mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

# Add executable bit for shebang files
# https://github.com/macournoyer/thin/pull/320
pushd %{buildroot}/%{gem_instdir}/example
chmod 755 async_chat.ru
chmod 755 async_tailer.ru
popd

%check
pushd .%{gem_instdir}

cp -a %{_builddir}/spec spec

# Depends on rubygem-benchmark_unit, not available in Fedora yet.
find spec/perf -name "*_spec.rb" -exec \
    sed -i '/be_faster_then/ i \    pending' {} \;

# The 'should force kill process in pid file' spec is not compatible with RSpec2.
# https://github.com/rspec/rspec-core/issues/520
sed -i -r "/'should (force )?kill process in pid file'/a \    pending" \
    spec/daemonizing_spec.rb

# To prevent timeout error on ppc64 arch.
sed -i '/^    def server_should_start_in_less_then/,/^    end/ s/(10)/(20)/' \
    spec/daemonizing_spec.rb

# These 2 tests are passing independently, but fails when running with the
# whole testsuite.
sed -i '/"tracing routines (with NO custom logger)"/a \    before { pending }' \
    spec/logging_spec.rb

rspec2 -I$(dirs +1)%{gem_extdir_mri} spec

popd

%files
%dir %{gem_instdir}
%{_bindir}/thin
%{gem_extdir_mri}
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/example/
%doc %{gem_instdir}/CHANGELOG
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 23 2020 Vít Ondruch <vondruch@redhat.com> - 1.7.2-12
- Fix FTBFS due maximum_connections changes.

* Fri Jan 17 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.7.2-12
- F-32: rebuild against ruby27

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 18 2019 Vít Ondruch <vondruch@redhat.com> - 1.7.2-9
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.6

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 1.7.2-6
- Rebuilt for switch to libxcrypt

* Thu Jan 04 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.7.2-5
- F-28: rebuild for ruby25

* Tue Aug 08 2017 Jun Aruga <jaruga@redhat.com> - 1.7.2-4
- Fix FTBFS.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Vít Ondruch <vondruch@redhat.com> - 1.7.2-1
- Update to Thin 1.7.2.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 10 2017 Vít Ondruch <vondruch@redhat.com> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.4

* Fri Jul 29 2016 Jun Aruga <jaruga@redhat.com> - 1.7.0-1
- Update to Thin 1.7.0.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 08 2016 Vít Ondruch <vondruch@redhat.com> - 1.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.3

* Tue Oct 20 2015 Vít Ondruch <vondruch@redhat.com> - 1.6.4-1
- Update to Thin 1.6.4.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jan 18 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.6.2-4
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_2.2
- Use rspec2 for now

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Vít Ondruch <vondruch@redhat.com> - 1.6.2-1
- Update to thin 1.6.2.

* Wed Apr 16 2014 Josef Stribny <jstribny@redhat.com> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.1

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 28 2013 Vít Ondruch <vondruch@redhat.com> - 1.5.0-1
- Update to thin 1.5.0.

* Thu Feb 28 2013 Vít Ondruch <vondruch@redhat.com> - 1.3.1-6
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb 01 2012 Vít Ondruch <vondruch@redhat.com> - 1.3.1-3
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Nov 25 2011 Vít Ondruch <vondruch@redhat.com> - 1.3.1-1
- Update to Thin 1.3.1.

* Tue Sep 06 2011 Chris Lalancette <clalance@redhat.com> - 1.2.11-10
- Bump the release so upgrades from F-16 work

* Mon Jul 25 2011 Chris Lalancette <clalance@redhat.com> - 1.2.11-3
- Move stats.html.erb to the main package (it is a runtime requirement)

* Fri Jul 22 2011 Chris Lalancette <clalance@redhat.com> - 1.2.11-2
- Fix the load path for thin_parser

* Tue Mar 01 2011 Michal Fojtik <mfojtik@redhat.com> - 1.2.11-1
- Version bump

* Tue Mar 01 2011 Michal Fojtik <mfojtik@redhat.com> - 1.2.8-3
- Removed Rake dependency completely

* Tue Mar 01 2011 Michal Fojtik <mfojtik@redhat.com> - 1.2.8-2
- Fixed RSpec tests

* Tue Mar 01 2011 Michal Fojtik <mfojtik@redhat.com> - 1.2.8-1
- Updated to upstream version

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 08 2010 Michal Fojtik <mfojtik@redhat.com> - 1.2.7-1
- Updated to upstream version

* Thu Feb 04 2010 Michal Fojtik <mfojtik@redhat.com> - 1.2.5-5
- Excluded ppc64 in tests (566401)
- Fixed Licensing

* Wed Feb 03 2010 Michal Fojtik <mfojtik@redhat.com> - 1.2.5-4
- Added rspec tests
- Fixed unwanted recompilation
- Fixed licensing

* Tue Feb 02 2010 Michal Fojtik <mfojtik@redhat.com> - 1.2.5-3
- Fixed description

* Tue Feb 02 2010 Michal Fojtik <mfojtik@redhat.com> - 1.2.5-2
- Build fixed
- Licence corrected
- Added missing requires
- Marked relevant files as documentation

* Tue Feb 02 2010 Michal Fojtik <mfojtik@redhat.com> - 1.2.5-1
- Initial package



# Generated from puma-3.6.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name puma

# Allow to use precompiled version of parser, because Ragel not always
# behaves correctly.
%bcond_without ragel
%bcond_without help2man

Name: rubygem-%{gem_name}
Version: 4.3.6
Release: 1%{?dist}
Summary: A simple, fast, threaded, and highly concurrent HTTP 1.1 server
License: BSD
URL: http://puma.io
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# The puma gem doesn't ship with the test suite.
# git clone https://github.com/puma/puma --no-checkout
# cd puma && git archive -v -o puma-4.3.6-tests.txz v4.3.6 test
Source1: %{gem_name}-%{version}-tests.txz
# The puma gem doesn't ship with the examples used in test suite.
# git archive -v -o puma-4.3.6-examples.txz v4.3.6 examples
Source3: %{gem_name}-%{version}-examples.txz
# Set the default cipher list "PROFILE=SYSTEM".
# https://fedoraproject.org/wiki/Packaging:CryptoPolicies
Patch2: rubygem-puma-3.6.0-fedora-crypto-policy-cipher-list.patch
# Don't exit Puma on test failure.
# https://github.com/puma/puma/pull/2332
Patch3: rubygem-puma-5.0.0-Report-pumactl-exit.patch
# Fix SSL certificates.
# https://github.com/puma/puma/pull/2333
Patch4: rubygem-puma-5.0.0-Update-test-certs-and-code.patch

# Git is needed just to apply Patch4.
BuildRequires: %{_bindir}/git
BuildRequires: openssl-devel
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby-devel
BuildRequires: rubygem(rack)
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(nio4r)
%if %{with ragel}
BuildRequires: %{_bindir}/ragel
%endif
%if %{with help2man}
BuildRequires: help2man
%endif
# Compiler is required for build of gem binary extension.
# https://fedoraproject.org/wiki/Packaging:C_and_C++#BuildRequires_and_Requires
BuildRequires: gcc

%description
Puma is a simple, fast, threaded, and highly concurrent HTTP 1.1 server for
Ruby/Rack applications. Puma is intended for use in both development and
production environments. It's great for highly concurrent Ruby implementations
such as Rubinius and JRuby as well as as providing process worker support to
support CRuby well.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version} -b 1 -b 3

%patch2 -p1

pushd %{_builddir}
%patch3 -p1

# When removed, remove also the `BR: git` above.
%global __scm git_am
%{expand:%__scm_setup_%{__scm}}
%apply_patch -p1 %{PATCH4}
popd

%if %{with ragel}
# Test suite on s390x fails on various places with following error:
# ext/puma_http11/http11_parser.rl:123: puma_parser_execute: Assertion `parser->nread <= len && "nread longer than length"' failed.
# Keep the upstream generated parser which appears to work.
# https://github.com/adrian-thurston/ragel/issues/51
%ifnarch s390x
# Regenarate the parser.
# https://fedoraproject.org/wiki/Packaging:Guidelines#Use_of_pregenerated_code
rm -f ext/puma_http11/http11_parser.c
ragel ext/puma_http11/http11_parser.rl -G2 -I ext/puma_http11 \
  -o ext/puma_http11/http11_parser.c
%endif
%endif

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

mkdir -p %{buildroot}%{gem_extdir_mri}/puma
cp -a .%{gem_extdir_mri}/gem.build_complete %{buildroot}%{gem_extdir_mri}/
cp -a .%{gem_extdir_mri}/puma/*.so %{buildroot}%{gem_extdir_mri}/puma

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/

mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

find %{buildroot}%{gem_instdir}/bin -type f | \
  xargs sed -i 's|^#!/usr/bin/env ruby$|#!/usr/bin/ruby|'

%if %{with help2man}
# Turn `puma --help` into man page.
export RUBYOPT="-I%{buildroot}%{gem_extdir_mri}:%{buildroot}%{gem_libdir}"
mkdir -p %{buildroot}%{_mandir}/man1
help2man --no-discard-stderr -N -s1 -o %{buildroot}%{_mandir}/man1/%{gem_name}.1 \
    %{buildroot}/usr/share/gems/gems/%{gem_name}-%{version}/bin/%{gem_name}
%endif


# Run the test suite
%check
pushd .%{gem_instdir}
ln -s %{_builddir}/test .
ln -s %{_builddir}/examples .

# We do not ship minitest-retry or minitest-proveit.
sed -i -e "/require..minitest\/\(retry\|proveit\)./ s/^/#/" test/helper.rb
sed -i "/Minitest::Retry/ s/^/#/" test/helper.rb
sed -i '/prove_it!/ s/^/#/' test/helper.rb

# Increase timeout seconds to avoid the timeout for every test case on Koji.
sed -i '/::Timeout.timeout/ s/60/600/' test/helper.rb

# Skip an unstable test on Koji.
# TestCLI#test_control failing with "pool_capacity": 0
# https://github.com/puma/puma/issues/2212
%ifarch ppc64le s390x aarch64
sed -i '/^  def test_control$/,/^  end$/ s/^/#/' test/test_cli.rb
%endif

# These test often timeouts on Koji.
sed -i '/^  def test_timeout_in_data_phase$/a\
    skip' test/test_puma_server.rb
sed -i '/^  def test_plugin$/a\
    skip' test/test_plugin.rb

# Skip a randomly failed SSL test.
# Errno::ECONNRESET: Connection reset by peer
#   /usr/share/ruby/openssl/buffering.rb:182:in `sysread_nonblock'
#   /usr/share/ruby/openssl/buffering.rb:182:in `read_nonblock'
sed -i '/^  def test_verify_fail_if_client_unknown_ca$/a\
    skip' test/test_puma_server_ssl.rb

# Skip unstable tests on Koji.
# test_integration_cluster.rb: not expected replies
# https://github.com/puma/puma/issues/2209
sed -i '/^  def test_usr1_all_respond_/a\
    skip' test/test_integration_cluster.rb

# Make binary exension available in Ruby load path.
# Enable verbose mode to check unstable tests easily.
RUBYOPT="-Ilib:$(dirs +1 -l)%{gem_extdir_mri}" CI=1 ruby \
  -e 'Dir.glob "./test/**/test_*.rb", &method(:require)' \
  -- -v

# Integration test
# Make binary exension available in Ruby load path.
RUBYOPT="-I$(dirs +1 -l)%{gem_extdir_mri}" ruby test/shell/run.rb

%if %{with help2man}
# Check `--help` output, using which man page is created
export RUBYOPT="-I%{buildroot}%{gem_extdir_mri}:%{buildroot}%{gem_libdir}"
%{buildroot}/usr/share/gems/gems/%{gem_name}-%{version}/bin/%{gem_name} --help 2> /dev/null \
  | grep -q '^puma <options> <rackup file>'
%endif
popd

%files
%dir %{gem_instdir}
%{_bindir}/puma
%{_bindir}/pumactl
%{gem_extdir_mri}
%license %{gem_instdir}/LICENSE
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%if %{with help2man}
%{_mandir}/man1/%{gem_name}.1*
%endif

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/History.md
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/docs
%{gem_instdir}/tools

%changelog
* Mon Sep 07 2020 Vít Ondruch <vondruch@redhat.com> - 4.3.6-1
- Update to Puma 4.3.6.
  Resolves: rhbz#1837148
  Resolves: rhbz#1863729
  Resolves: rbhz#1842535
  Resolves: rbhz#1842540
- Fix the man pages generation and move them into the main package.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.3-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Mar 31 2020 Jun Aruga <jaruga@redhat.com> - 4.3.3-1
- Update to puma 4.3.3.
- Fix newline characters to insert malicious content (CVE-2020-5247).
- Fix carriage return character to insert malicious content (CVE-2020-5249).

* Fri Jan 31 2020 Pavel Valena <pvalena@redhat.com> - 4.3.1-1
- Update to puma 4.3.1.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Vít Ondruch <vondruch@redhat.com> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.7

* Wed Aug 21 2019 Pavel Valena <pvalena@redhat.com> - 4.1.0-1
- Update to puma 4.1.0.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jan 30 2019 Vít Ondruch <vondruch@redhat.com> - 3.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.6

* Tue Sep 25 2018 Vít Ondruch <vondruch@redhat.com> - 3.12.0-1
- Update to Puma 3.12.0.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 29 2018 Pavel Valena <pvalena@redhat.com> - 3.11.4-1
- Update to puma 3.11.4.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 3.11.0-2
- Rebuilt for switch to libxcrypt

* Thu Jan 04 2018 Vít Ondruch <vondruch@redhat.com> - 3.11.0-1
- Update to Puma 3.11.0.

* Thu Jan 04 2018 Vít Ondruch <vondruch@redhat.com> - 3.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.5

* Mon Aug 21 2017 Jun Aruga <jaruga@redhat.com> - 3.10.0-3
- Skip unstable test.

* Mon Aug 21 2017 Jun Aruga <jaruga@redhat.com> - 3.10.0-2
- Fix for unstable test.

* Fri Aug 18 2017 Jun Aruga <jaruga@redhat.com> - 3.10.0-1
- Update to Puma 3.10.0.

* Wed Aug 09 2017 Jun Aruga <jaruga@redhat.com> - 3.9.1-1
- Update to Puma 3.9.1.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 28 2017 Jun Aruga <jaruga@redhat.com> - 3.8.2-1
- Update to Puma 3.8.2.

* Thu Feb 16 2017 Jun Aruga <jaruga@redhat.com> - 3.7.0-1
- Update to Puma 3.7.0.
- Remove README.Fedora, as the content is already mentioned in README.md
- Comment out for ragel's build error on buildArch: armv7hl.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 16 2017 Vít Ondruch <vondruch@redhat.com> - 3.6.2-1
- Update to Puma 3.6.2.

* Wed Nov 23 2016 Jun Aruga <jaruga@redhat.com> - 3.6.0-4
- Use OpenSSL 1.0 instead of OpenSSL 1.1 (rhbz#1397809)

* Wed Sep 21 2016 Jun Aruga <jaruga@redhat.com> - 3.6.0-3
- Skip test that needs internet.

* Mon Sep 19 2016 Jun Aruga <jaruga@redhat.com> - 3.6.0-2
- Add openssl-devel dependency to enable HTTPS support.
- Add regenerated parser logic.
- Improve Ruby load path to run test suite.
- Improve files section.

* Thu Aug 11 2016 Jun Aruga <jaruga@redhat.com> - 3.6.0-1
- Initial package

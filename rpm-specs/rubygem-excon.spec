%global gem_name excon

Name: rubygem-%{gem_name}
Version: 0.73.0
Release: 2%{?dist}
Summary: Speed, persistence, http(s)
License: MIT
URL: https://github.com/excon/excon
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/excon/excon.git && cd excon
# git archive -v -o excon-0.73.0-tests.tar.gz v0.73.0 spec/ tests/
Source1: %{gem_name}-%{version}-tests.tar.gz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: %{_bindir}/openssl
BuildRequires: %{_bindir}/rackup
BuildRequires: %{_bindir}/shindo
BuildRequires: rubygem(activesupport)
BuildRequires: rubygem(delorean)
BuildRequires: rubygem(eventmachine)
BuildRequires: rubygem(open4)
BuildRequires: rubygem(puma)
BuildRequires: rubygem(sinatra)
BuildRequires: rubygem(rspec)
BuildArch: noarch

%description
EXtended http(s) CONnections.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version} -b 1

# Use system crypto policies.
# https://fedoraproject.org/wiki/Packaging:CryptoPolicies
sed -i "/ciphers/ s/'.*'/'PROFILE=SYSTEM'/" lib/excon/constants.rb

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

# Kill bundled cacert.pem
rm -rf %{buildroot}%{gem_instdir}/data

%check
pushd .%{gem_instdir}

# Move the tests into place
ln -s %{_builddir}/spec spec
ln -s %{_builddir}/tests tests

# Unicorn is not available in Fedora yet (rhbz#1065685).
sed -i '/if plugin == :unicorn/ i\  before { skip("until #{plugin} is in Fedora") } if plugin == :unicorn' spec/support/shared_contexts/test_server_context.rb
sed -i '/with_unicorn/ s/^/  pending\n\n/' tests/{basic_tests.rb,proxy_tests.rb}

rspec spec

# Don't use Bundler.
sed -i "/'bundler\/setup'/ s/^/#/" tests/test_helper.rb

# This would require sinatra-contrib.
sed -i '/redirecting_with_cookie.ru/,/^  end/ s/^/#/' tests/middlewares/capture_cookies_tests.rb

# Keep the test certificates fresh.
# https://github.com/excon/excon/blob/9e934d0dc169ddfd1fe08e07873a5ba2d8be7aa1/Rakefile#L27-L28
openssl req -subj '/CN=excon/O=excon' -new -newkey rsa:2048 -sha256 -days 365 -nodes -x509 -keyout tests/data/excon.cert.key -out tests/data/excon.cert.crt
openssl req -subj '/CN=127.0.0.1/O=excon' -new -newkey rsa:2048 -sha256 -days 365 -nodes -x509 -keyout tests/data/127.0.0.1.cert.key -out tests/data/127.0.0.1.cert.crt

shindo
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE.md
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CONTRIBUT*
%doc %{gem_instdir}/README.md
%{gem_instdir}/excon.gemspec

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.73.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Apr 24 2020 Vít Ondruch <vondruch@redhat.com> - 0.73.0-1
- Update to excon 0.73.0.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.62.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.62.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 05 2019 Vít Ondruch <vondruch@redhat.com> - 0.62.0-2
- Fix Ruby 2.6 test failure.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.62.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 10 2018 Vít Ondruch <vondruch@redhat.com> - 0.62.0-1
- Update to excon 0.62.0.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.60.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.60.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Dec 19 2017 Vít Ondruch <vondruch@redhat.com> - 0.60.0-1
- Update to excon 0.60.0.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.54.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.54.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 05 2017 Vít Ondruch <vondruch@redhat.com> - 0.54.0-1
- Update to excon 0.54.0.

* Thu Sep 08 2016 Vít Ondruch <vondruch@redhat.com> - 0.52.0-1
- Update to excon 0.52.0.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.45.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 21 2015 Vít Ondruch <vondruch@redhat.com> - 0.45.4-1
- Update to excon 0.45.4.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.45.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar 27 2015 Vít Ondruch <vondruch@redhat.com> - 0.45.1-1
- Update to excon 0.45.1.

* Mon Sep 29 2014 Brett Lentz <blentz@redhat.com> - 0.39.6-1
- Update to excon 0.39.6.

* Wed Jul 30 2014 Brett Lentz <blentz@redhat.com> - 0.38.0-1
- Update to excon 0.38.0.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.33.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Vít Ondruch <vondruch@redhat.com> - 0.33.0-1
- Update to excon 0.33.0.

* Wed Oct 09 2013 Josef Stribny <jstribny@redhat.com> - 0.25.3-1
- Update to excon 0.25.3.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 14 2013 Vít Ondruch <vondruch@redhat.com> - 0.21.0-1
- Update to excon 0.21.0.

* Fri Mar 08 2013 Vít Ondruch <vondruch@redhat.com> - 0.16.7-3
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 09 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.16.7-1
- Update to Excon 0.16.7.

* Mon Jul 23 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.14.3-1
- Update to Excon 0.14.3.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 25 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.14.1-1
- Update to Excon 0.14.1
- Removed no longer needed patch for downgrading dependencies.
- Remove newly bundled certificates and link to system ones.

* Wed Feb 01 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.9.5-2
- Fixed the changelog.

* Wed Feb 01 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.9.5-1
- Update to version 0.9.5
- Fixed the dependencies for the new version.

* Mon Dec 05 2011 Bohuslav Kabrda <bkabrda@redhat.com> - 0.7.12-1
- Update to version 0.7.12.

* Mon Nov 28 2011 Bohuslav Kabrda <bkabrda@redhat.com> - 0.7.8-1
- Update to version 0.7.8.
- Replaced defines with more appropriate globals.
- Added Build dependency on rubygem-eventmachine.
- Fixed running tests for the new version.

* Wed Oct 12 2011 bkabrda <bkabrda@redhat.com> - 0.7.6-1
- Update to version 0.7.6
- Introduced doc subpackage
- Introduced check section

* Tue Jul 05 2011 Chris Lalancette <clalance@redhat.com> - 0.6.3-1
- Initial package

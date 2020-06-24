# Generated from faraday-0.8.7.gem by gem2rpm -*- rpm-spec -*-
%global gem_name faraday

Name: rubygem-%{gem_name}
Version: 0.15.4
Release: 3%{?dist}
Summary: HTTP/REST API client library
License: MIT
URL: https://github.com/lostisland/faraday
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/lostisland/faraday.git && cd faraday
# git checkout v0.15.4 && tar czvf faraday-0.15.4-tests.tgz test/ script/
Source1: %{gem_name}-%{version}-tests.tgz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 1.9
BuildRequires: %{_bindir}/lsof
BuildRequires: rubygem(minitest)
BuildRequires: rubygem(multipart-post)
BuildRequires: rubygem(sinatra)
# Adapter test dependencies, might be optionally disabled.
BuildRequires: rubygem(em-http-request)
BuildRequires: rubygem(excon)
BuildRequires: rubygem(httpclient)
BuildRequires: rubygem(net-http-persistent)
BuildRequires: rubygem(rack-test)
BuildRequires: rubygem(typhoeus)
BuildArch: noarch

%description
HTTP/REST API client library.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version} -b 1

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
ln -s %{_builddir}/test test
ln -s %{_builddir}/script script

# Avoid Bundler.
sed -i '/bundler\/setup/,/^fi$/ s/^/#/' script/test

# Follow symlinks.
sed -i "s/find /find -L /" script/test

# We don't care about code coverage.
sed -i "/simplecov/,/^end$/ s/^/#/" test/helper.rb

# We don't have {patron,em-synchrony} available in Fedora.
mv test/adapters/em_synchrony_test.rb{,.disabled}
mv test/adapters/patron_test.rb{,.disabled}

# Rrequirs internet access.
sed -i "/def test_dynamic_no_proxy/a\      skip" test/connection_test.rb

# Fails with Typhoeus 1.0.2
sed -i "/def test_custom_adapter_config/a\      skip" test/adapters/typhoeus_test.rb

RUBYOPT="-Ilib -ryaml" script/test
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE.md
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 01 2019 Vít Ondruch <vondruch@redhat.com> - 0.15.4-1
- Update to Faraday 0.15.4.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 17 2014 Achilleas Pipinellis <axilleas@fedoraproject.org> - 0.9.0-1
- Bump to 0.9.0
- Remove unessecary files

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Nov 17 2013 Achilleas Pipinellis <axilleaspi@ymail.com> - 0.8.8-2
- Remove multibytes.txt
- Remove Gemfile, Rakefile from doc macro

* Sun Aug 04 2013 Anuj More - 0.8.8-1
- From 0.8.7 to 0.8.8

* Tue May 14 2013 Anuj More - 0.8.7-1
- Initial package

# Generated from faraday-0.8.7.gem by gem2rpm -*- rpm-spec -*-
%global gem_name faraday

Name: rubygem-%{gem_name}
Version: 1.0.1
Release: 1%{?dist}
Summary: HTTP/REST API client library
License: MIT
URL: https://lostisland.github.io/faraday
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Since we don't have multipart-parser in Fedora, include the essential part
# just for testing purposes.
# https://github.com/danabr/multipart-parser/blob/master/lib/multipart_parser/parser.rb
Source1: https://raw.githubusercontent.com/danabr/multipart-parser/master/lib/multipart_parser/parser.rb
# https://github.com/danabr/multipart-parser/blob/master/lib/multipart_parser/reader.rb
Source2: https://raw.githubusercontent.com/danabr/multipart-parser/master/lib/multipart_parser/reader.rb
# Fix Rack 2.1+ test compatibility.
# https://github.com/lostisland/faraday/pull/1171
Patch0: rubygem-faraday-1.0.1-Properly-fix-test-failure-with-Rack-2.1.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.3
BuildRequires: rubygem(multipart-post)
BuildRequires: rubygem(rack)
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(webmock)
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
mkdir -p multipart_parser/multipart_parser
cp %{SOURCE1} %{SOURCE2} multipart_parser/multipart_parser

%setup -q -n %{gem_name}-%{version}

%patch0 -p1

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
# We don't care about code coverage.
sed -i "/simplecov/ s/^/#/" spec/spec_helper.rb
sed -i "/coveralls/ s/^/#/" spec/spec_helper.rb
sed -i "/SimpleCov/,/^end$/ s/^/#/" spec/spec_helper.rb

# We don't need Pry.
sed -i "/pry/ s/^/#/" spec/spec_helper.rb

# We don't have {patron,em-synchrony} available in Fedora.
mv spec/faraday/adapter/em_synchrony_spec.rb{,.disabled}
mv spec/faraday/adapter/patron_spec.rb{,.disabled}

# This needs http-net-persistent 3.0+.
sed -i '/allows to set min_version in SSL settings/a\      skip' \
  spec/faraday/adapter/net_http_persistent_spec.rb

rspec -I%{_builddir}/multipart_parser -rspec_helper -r%{SOURCE1} spec -f d
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE.md
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/examples
%{gem_instdir}/spec

%changelog
* Thu Jul 23 2020 Vít Ondruch <vondruch@redhat.com> - 1.0.1-1
- Update to Faraday 1.0.1.
  Resolves: rhbz#1756449

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

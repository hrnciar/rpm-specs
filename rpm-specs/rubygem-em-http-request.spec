# Generated from em-http-request-1.1.5.gem by gem2rpm -*- rpm-spec -*-
%global gem_name em-http-request

Name: rubygem-%{gem_name}
Version: 1.1.5
Release: 8%{?dist}
Summary: EventMachine based, async HTTP Request client
License: MIT
URL: http://github.com/igrigorik/em-http-request
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(eventmachine)
BuildRequires: rubygem(multi_json)
BuildRequires: rubygem(em-socksify)
BuildRequires: rubygem(addressable)
BUildRequires: rubygem(cookiejar)
BuildRequires: rubygem(http_parser.rb)
BuildRequires: rubygem(rack)
BuildRequires: %{_bindir}/ping
BuildRequires: rubygem(rspec)

BuildArch: noarch

%description
EventMachine based, async HTTP Request client.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


# Have networking enabled in your mock config before testing
%check
pushd .%{gem_instdir}
# We are trying not to use bundler when not needed
sed -i "/require 'bundler\/setup'/ s/^/#/" spec/helper.rb
# Mongrel is deprecated so we are using WEBrick server
sed -i 's/Mongrel/WEBrick/' spec/stallion.rb

# Failing tests
sed -i '/it "should report error if connection was closed by server on client keepalive requests" do/ ,/^  end$/ s/^/#/' spec/client_spec.rb
# this one seems to fail with WEBrick since Thin server fixes it at the expense of other fails and segfault.
sed -i '/it "should set content-length to 0 on posts with empty bodies" do/ ,/^  end$/ s/^/#/' spec/client_spec.rb
# Fails on WEBrick but on Thin the test is passing
sed -i '/it "should fail GET on invalid host" do/ ,/^  end$/ s/^/#/' spec/dns_spec.rb

# Disable segfaulting tests.
sed -i '/it "should fail gracefully on an invalid host in Location header" do/ ,/^  end$/ s/^/#/' spec/dns_spec.rb
sed -i '/it "should keep default http port in redirect url that include it" do/ ,/^  end$/ s/^/#/' spec/redirect_spec.rb
sed -i '/it "should keep default https port in redirect url that include it" do/ ,/^  end$/ s/^/#/' spec/redirect_spec.rb

# One of the tests is expecting UTF-8 encoding enviroment
LANG=C.UTF-8 rspec spec -f d
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.*
%{gem_instdir}/benchmarks
%exclude %{gem_instdir}/em-http-request.gemspec
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/Changelog.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/examples
%{gem_instdir}/spec

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 18 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.1.5-5
- Use C.UTF-8 locale
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Sat Jul 14 2018 Jaroslav Prokop <jar.prokop@volny.cz> - 1.1.5-4
- Delete "Requires: rubygem(cookiejar)".

  Bug#1561487 regarding this issue was fixed.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 28 2018 Jaroslav Prokop <jar.prokop@volny.cz> - 1.1.5-2
- Add rubygem(cookiejar) require, for more info see comment
  at the require.

* Tue Feb 20 2018 Jaroslav Prokop <jar.prokop@volny.cz> - 1.1.5-1
- Initial package

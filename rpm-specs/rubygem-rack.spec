%global gem_name rack

# There is circular dependency between thin and rack.
%bcond_with bootstrap

Name: rubygem-%{gem_name}
Version: 2.2.3
# Introduce Epoch (related to bug 552972)
Epoch:  1
Release: 1%{?dist}
Summary: A modular Ruby webserver interface
# lib/rack/show_{status,exceptions}.rb contains snippets from Django under BSD license.
License: MIT and BSD
URL: https://rack.github.io/
Source0: https://rubygems.org/downloads/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.2.2
BuildRequires: rubygem(concurrent-ruby)
BuildRequires: memcached
BuildRequires: rubygem(memcache-client)
BuildRequires: rubygem(minitest)
%if ! %{with bootstrap}
BuildRequires: rubygem(thin)
%endif
BuildArch: noarch

%global __brp_mangle_shebangs_exclude_from ^%{gem_instdir}/test/cgi/test.ru$

%description
Rack provides a minimal, modular and adaptable interface for developing
web applications in Ruby.  By wrapping HTTP requests and responses in
the simplest way possible, it unifies and distills the API for web
servers, web frameworks, and software in between (the so-called
middleware) into a single method call.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

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


mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x
find %{buildroot}%{gem_instdir}/{bin,test/cgi} -type f | \
  xargs sed -i 's|^#!/usr/bin/env ruby$|#!/usr/bin/ruby|'

# Fix anything executable that does not have a shebang
for file in `find %{buildroot}/%{gem_instdir} -type f -perm /a+x`; do
    [ -z "`head -n 1 $file | grep \"^#!/\"`" ] && chmod -v 644 $file
done

# Find files with a shebang that do not have executable permissions
for file in `find %{buildroot}%{gem_instdir} -type f`; do
    [ ! -z "`head -n 1 $file | grep \"^#!\"`" ] && chmod -v 755 $file
done

%check
# at version 2.1.1 are currently no tests available
pushd .%{gem_instdir}

# During the building on mock environment, the testing process id 1 is owned
# by running user mockbuild's command STUBINIT, though it is owned by root user
# on usual environment.
# The server status does not return ":not_owned".
#sed -i '/^  it "check pid file presence and not owned process" do$/,/^  end$/ s/^/#/' \
#  test/spec_server.rb

# Get temporary PID file name and start memcached daemon.
PID=%(mktemp)
memcached -d -P "$PID"

# Rack::Session::Memcache#test_0009_maintains freshness
# requires encoding set to UTF-8:
# https://github.com/rack/rack/issues/1305
LC_ALL=C.UTF-8 \
ruby -Ilib:test -e 'Dir.glob "./test/spec_*.rb", &method(:require)'

# Kill memcached daemon.
kill -TERM $(< "$PID")

popd

%files
%dir %{gem_instdir}
%{_bindir}/rackup
%license %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%{gem_instdir}/bin
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.rdoc
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/SPEC.rdoc
%{gem_instdir}/Rakefile
%{gem_instdir}/%{gem_name}.gemspec
%doc %{gem_instdir}/example
%doc %{gem_instdir}/contrib
# at version 2.1.1 are currently no tests available
#{gem_instdir}/test

%changelog
* Wed Jun 17 2020 Gerd Pokorra <gp@zimt.uni-siegen.de> - 1:2.2.3-1
- Update to Rack 2.2.3

* Mon Feb 17 2020 Gerd Pokorra <gp@zimt.uni-siegen.de> - 1:2.2.2-1
- Update to Rack 2.2.2

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 13 2020 Gerd Pokorra <gp@zimt.uni-siegen.de> - 1:2.1.1-1
- Update to Rack 2.1.1
- This version has no files for tests included 

* Thu Dec 19 2019 Pavel Valena <pvalena@redhat.com> - 1:2.0.8-1
- Update to Rack 2.0.8.
- Change the source URL

* Wed Jul 24 2019 Pavel Valena <pvalena@redhat.com> - 1:2.0.7-1
- Update to Rack 2.0.7.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 18 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1:2.0.6-3
- Use C.UTF-8 locale
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Mon Nov 12 2018 Vít Ondruch <vondruch@redhat.com> - 2.0.6-1
- Update to Rack 2.0.6.

* Mon Sep 24 2018 pvalena <pvalena@redhat.com> - 1:2.0.5-1
- Update to rack 2.0.5.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 15 2018 Vít Ondruch <vondruch@redhat.com> - 1:2.0.4-2
- Exclude test.ru shebang from being mangled.

* Tue Feb 13 2018 Jun Aruga <jaruga@redhat.com> - 1:2.0.4-1
- Update to Rack 2.0.4.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 09 2017 Jun Aruga <jaruga@redhat.com> - 1:2.0.3-2
- Improve bootstrapping logic.
  Ref: https://fedoraproject.org/wiki/Packaging:Guidelines#Bootstrapping
- Fix wrong script interpreter for rpmlint.

* Thu Jun 01 2017 Steve Traylen <steve.traylen@cern.ch> - 1:2.0.3-1
- Update to Rack 2.0.3.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 09 2017 Vít Ondruch <vondruch@redhat.com> - 1:2.0.1-2
- Fix test error caused by rubygem-concurrent-ruby.

* Fri Jul 01 2016 Vít Ondruch <vondruch@redhat.com> - 1:2.0.1-1
- Update to Rack 2.0.1.

* Mon May 02 2016 Jun Aruga <jaruga@redhat.com> - 1:1.6.4-1
- Update to 1.6.4.
- Fix test suite for FTBFS (rhbz#1308069).

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Vít Ondruch <vondruch@redhat.com> - 1:1.6.2-1
- Update to Rack 1.6.2.

* Tue Jun 2 2015 Steve Traylen <jstribny@redhat.com> - 1:1.6.1-1
- Update to 1.6.1

* Mon Feb 09 2015 Josef Stribny <jstribny@redhat.com> - 1:1.6.0-1
- Update to 1.6.0

* Thu Sep 25 2014 Steve Traylen <steve.traylen@cern.ch> - 1:1.5.2-4
- Add enable_check flag and disable check for .el7.
- Rely on autorequires and autoprovides.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Feb 05 2014  Josef Stribny <jstribny@redhat.com> - 1:1.5.2-2
- Fix licensing
- Add virtual provide for bundled okjson

* Wed Jul 24 2013 Josef Stribny <jstribny@redhat.com> - 1:1.5.2-1
- Update to rack 1.5.2

* Fri Mar 01 2013 Vít Ondruch <vondruch@redhat.com> - 1:1.4.5-3
- Enable thin test suite.

* Mon Feb 25 2013 Vít Ondruch <vondruch@redhat.com> - 1:1.4.5-2
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Fri Feb 08 2013 Josef Stribny <jstribny@redhat.com> - 1:1.4.5-1
- Update to Rack 1.4.5.

* Tue Jan 15 2013 Vít Ondruch <vondruch@redhat.com> - 1:1.4.4-1
- Update to Rack 1.4.4.

* Thu Nov 01 2012 Vít Ondruch <vondruch@redhat.com> - 1:1.4.1-2
- Fixed epoch in -doc sub-package.

* Mon Oct 29 2012 Vít Ondruch <vondruch@redhat.com> - 1:1.4.1-1
- Update to Rack 1.4.1.
- Documentation moved into subpackage.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 24 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1:1.4.0-2
- Rebuilt for Ruby 1.9.3.

* Thu Jan 05 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1:1.4.0-1
- Update to Rack 1.4.
- Moved gem install to %%prep to be able to apply patches.
- Applied two patches that fix test failures with Ruby 1.8.7-p357.

* Tue Jun 28 2011 Vít Ondruch <vondruch@redhat.com> - 1:1.3.0-1
- Updated to Rack 1.3.
- Fixed FTBFS.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Mar 11 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1:1.1.0-2
- Epoch 1 for keeping upgrade path from F-12 (related to bug 552972)
- Enable %%check

* Mon Jan  4 2010 Jeroen van Meeuwen <kanarip@kanarip.com> - 1.1.0-1
- New upstream version

* Sun Oct 25 2009 Jeroen van Meeuwen <kanarip@kanarip.com> - 1.0.1-1
- New upstream version

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Apr 26 2009 Jeroen van Meeuwen <kanarip@fedoraproject.org> - 1.0.0-1
- New upstream version

* Mon Mar 16 2009 Jeroen van Meeuwen <j.van.meeuwen@ogd.nl> - 0.9.1-1
- New upstream version

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Nov 09 2008 Jeroen van Meeuwen <j.van.meeuwen@ogd.nl> - 0.4.0-2
- Remove unused macro (#470694)
- Add ruby(abi) = 1.8 as required by package guidelines (#470694)
- Move %%{gem_dir}/bin/rackup to %%{_bindir} (#470694)

* Sat Nov 08 2008 Jeroen van Meeuwen <j.van.meeuwen@ogd.nl> - 0.4.0-1
- Initial package

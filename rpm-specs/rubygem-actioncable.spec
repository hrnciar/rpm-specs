# Generated from actioncable-5.0.0.rc2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name actioncable

# Disabling JS recompilation might significantly reduce the amount of
# build dependencies.
%global recompile_js 1

Name: rubygem-%{gem_name}
Version: 5.2.3
Release: 3%{?dist}
Summary: WebSocket framework for Rails
License: MIT
URL: http://rubyonrails.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/rails/rails.git && cd rails/actioncable
# git checkout v5.2.3 && tar czvf actioncable-5.2.3-tests.tgz test/
Source1: %{gem_name}-%{version}-tests.tgz
# The source code of pregenerated JS files.
# git clone https://github.com/rails/rails.git && cd rails/actioncable
# git checkout v5.2.3 && tar czvf actioncable-5.2.3-app.tgz app/
Source2: %{gem_name}-%{version}-app.tgz
# Recompile with script extracted from
# https://github.com/rails/rails/blob/71d406697266fc2525706361b86aeb85183fe4c7/actioncable/Rakefile
Source3: recompile_js.rb
BuildRequires: ruby(release)
BuildRequires: rubygems-devel > 1.3.1
BuildRequires: ruby >= 2.2.2
BuildRequires: rubygem(actionpack) = %{version}
BuildRequires: rubygem(mocha)
BuildRequires: rubygem(nio4r)
BuildRequires: rubygem(puma)
BuildRequires: %{_bindir}/redis-server
BuildRequires: rubygem(redis)
BuildRequires: rubygem(websocket-driver)
%if 0%{?recompile_js} > 0
BuildRequires: rubygem(coffee-script)
BuildRequires: rubygem(sprockets)
BuildRequires: %{_bindir}/node
%endif
BuildArch: noarch

%description
Structure many real-time application concerns into channels over a single
WebSocket connection.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version} -a 2

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
%if 0%{?recompile_js} > 0
# Recompile the embedded JS file from CoffeeScript sources.
#
# This is practice suggested by packaging guidelines:
# https://fedoraproject.org/wiki/Packaging:Guidelines#Use_of_pregenerated_code

cp -a %{SOURCE3} .

# Remove folder to ensure JS is recompiled
rm -rf lib/assets/compiled
RUBYOPT=-Ilib ruby recompile_js.rb
%endif

# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


%check
pushd .%{gem_instdir}
tar xzvf %{SOURCE1}

# We don't have websocket-client-simple in Fedora yet.
mv test/client_test.rb{,.disable}

# TODO: Needs AR together with PostgreSQL.
mv test/subscription_adapter/postgresql_test.rb{,.disable}

# Start a testing Redis server instance
REDIS_DIR=$(mktemp -d)
redis-server --dir $REDIS_DIR --pidfile $REDIS_DIR/redis.pid --daemonize yes

ruby -Ilib:test -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'

# Shutdown Redis.
kill -INT $(cat $REDIS_DIR/redis.pid)

# TODO: Enable the test/javascript test cases.
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar 28 2019 Pavel Valena <pvalena@redhat.com> - 5.2.3-1
- Update to Action Cable 5.2.3.

* Thu Mar 14 2019 Pavel Valena <pvalena@redhat.com> - 5.2.2.1-1
- Update to Action Cable 5.2.2.1.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 05 2018 Pavel Valena <pvalena@redhat.com> - 5.2.2-1
- Update to Action Cable 5.2.2.

* Wed Aug 08 2018 Pavel Valena <pvalena@redhat.com> - 5.2.1-1
- Update to Action Cable 5.2.1.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 01 2018 Pavel Valena <pvalena@redhat.com> - 5.2.0-1
- Update to Action Cable 5.2.0.

* Fri Feb 16 2018 Pavel Valena <pvalena@redhat.com> - 5.1.5-1
- Update to Action Cable 5.1.5.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Sep 11 2017 Pavel Valena <pvalena@redhat.com> - 5.1.4-1
- Update to Action Cable 5.1.4.

* Tue Aug 08 2017 Pavel Valena <pvalena@redhat.com> - 5.1.3-1
- Update to Action Cable 5.1.3.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 Pavel Valena <pvalena@redhat.com> - 5.1.2-1
- Update to Action Cable 5.1.2.

* Mon May 22 2017 Pavel Valena <pvalena@redhat.com> - 5.1.1-1
- Update to Action Cable 5.1.1.

* Thu Mar 02 2017 Pavel Valena <pvalena@redhat.com> - 5.0.2-1
- Update to Action Cable 5.0.2.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 03 2017 Pavel Valena <pvalena@redhat.com> - 5.0.1-2
- Enable JS recompilation.
- Use recompile script from previous Action Cable version

* Mon Jan 02 2017 Pavel Valena <pvalena@redhat.com> - 5.0.1-1
- Update to Action Cable 5.0.1.
- Disable JS recompilation.

* Tue Aug 16 2016 Pavel Valena <pvalena@redhat.com> - 5.0.0.1-1
- Update to Actioncable 5.0.0.1

* Thu Jun 30 2016 Vít Ondruch <vondruch@redhat.com> - 5.0.0-1
- Initial package

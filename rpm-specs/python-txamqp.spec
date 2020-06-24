%global upstream_name txamqp

Name:           python-%{upstream_name}
Version:        0.8.1
Release:        13%{?dist}
Summary:        A Python library for communicating with AMQP peers and brokers using Twisted

License:        ASL 2.0
URL:            https://github.com/txamqp/txamqp
Source0:        https://files.pythonhosted.org/packages/source/t/txAMQP/txAMQP-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%global _description\
txAMQP is a Python library for communicating with AMQP peers and brokers using\
Twisted.\
\
This project contains all the necessary code to connect, send and receive\
messages to/from an AMQP-compliant peer or broker (Qpid, OpenAMQ, RabbitMQ)\
using Twisted.

%description %_description

%package -n python3-%{upstream_name}
Summary:        Python 3 library for communicating with AMQP peers and brokers using Twisted
Requires:       python3-twisted
Requires:       amqp
%{?python_provide:%python_provide python3-%{upstream_name}}

%description -n python3-%{upstream_name} %_description

# Currently missing python3-thrift: https://bugzilla.redhat.com/show_bug.cgi?id=1533306
%if 0
%package -n python3-%{upstream_name}-thrift
Summary:        Contributed Thrift libraries for Twisted (Python 3)
Requires:       python3-%{upstream_name} = %{version}-%{release}
Requires:       python3-thrift
%{?python_provide:%python_provide python3-%{upstream_name}-thrift}

%description -n python3-%{upstream_name}-thrift
txAMQP also includes support for using Thrift RPC over AMQP in Twisted
applications.
%endif

%prep
%setup -q -n txAMQP-%{version}
# Fix non-executable-script error
sed -i '/^#!\/usr\/bin\/env python/,+1 d' src/txamqp/codec.py

%build
%{py3_build}

%install
%{py3_install}

%files -n python3-%{upstream_name}
%doc LICENSE
%{python3_sitelib}/%{upstream_name}
%exclude %{python3_sitelib}/%{upstream_name}/contrib/thrift
%{python3_sitelib}/txAMQP-%{version}-*.egg-info

%if 0
%files -n python3-%{upstream_name}-thrift
%{python3_sitelib}/%{upstream_name}/contrib/thrift
%endif

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8.1-13
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.1-11
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.1-10
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 17 2018 Miro Hrončok <mhroncok@redhat.com> - 0.8.1-7
- Remove Python 2 subpackages (#1627304)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.8.1-5
- Rebuilt for Python 3.7

* Fri Mar 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.8.1-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Dan Callaghan <dcallagh@redhat.com> - 0.8.1-2
- Disabled python3-txamqp-thrift subpackage until python3-thrift is available

* Mon Jan 08 2018 Dan Callaghan <dcallagh@redhat.com> - 0.8.1-1
- Upstream release 0.8.1 (with Python 3 support)

* Sun Dec 17 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.7.0-5
- Also rename the binary thrift subpackage to python2-txamqp-thrift

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.7.0-4
- Python 2 binary package renamed to python2-txamqp
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Apr 03 2017 Dan Callaghan <dcallagh@redhat.com> - 0.7.0-2
- Fix dependency on python2-twisted

* Fri Mar 31 2017 Dan Callaghan <dcallagh@redhat.com> - 0.7.0-1
- Upstream bug fix release 0.7.0

* Fri Mar 31 2017 Dan Callaghan <dcallagh@redhat.com> - 0.6.2-6
- Fix dependency on python2-thrift

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 09 2015 Dan Callaghan <dcallagh@redhat.com> - 0.6.2-1
- Fragment body if the content frame exceeds the negotiated max fram length.
- Use AMQPLAIN by default.
- Added method callback to catch channel_close errors.
- Added MANIFEST.in file with LICENSE.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 27 2012 Silas Sewell <silas@sewell.org> - 0.6.1-1
- Update to 0.6.1

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Sep 12 2010 Silas Sewell <silas@sewell.ch> - 0.3-1
- Initial build

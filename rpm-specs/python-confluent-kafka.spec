%if 0%{?fedora} || 0%{?rhel} > 7
%bcond_with    python2
%bcond_without python3
%else
%bcond_without python2
%bcond_with    python3
%endif

%global pypi_name confluent-kafka

Name:           python-%{pypi_name}
Version:        0.11.6
Release:        10%{?dist}
Summary:        Confluent's Apache Kafka client for Python

License:        ASL 2.0
URL:            https://github.com/confluentinc/confluent-kafka-python
Source0:        https://files.pythonhosted.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

%description
confluent-kafka-python is Confluent's Python client for Apache Kafka
and the Confluent Platform.

%if %{with python2}
%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}
BuildRequires:  gcc
BuildRequires:  librdkafka-devel
BuildRequires:  python2-devel
# Unit tests are present in the upstream repo, but not in the PyPi distribution
# https://github.com/confluentinc/confluent-kafka-python/issues/508
#BuildRequires:  python2dist(pytest)
BuildRequires:  python2-setuptools

Requires:       python2-fastavro
%if 0%{?fedora} || 0%{?rhel} > 7
Requires:       python2-enum34
%else
Requires:       python-enum34
%endif
Requires:       python2-futures
Requires:       python2-requests
Requires:       librdkafka >= 0.11.6
%description -n python2-%{pypi_name}
confluent-kafka-python is Confluent's Python client for Apache Kafka
and the Confluent Platform.

%endif

%if %{with python3}
%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
BuildRequires:  gcc
BuildRequires:  librdkafka-devel
BuildRequires:  python3-devel
# Unit tests are present in the upstream repo, but not in the PyPi distribution
# https://github.com/confluentinc/confluent-kafka-python/issues/508
#BuildRequires:  python3dist(pytest)
BuildRequires:  python3-setuptools
BuildRequires:  /usr/bin/pathfix.py

Requires:       python3-fastavro
Requires:       python3-requests
Requires:       librdkafka >= 0.11.6
%description -n python3-%{pypi_name}
confluent-kafka-python is Confluent's Python client for Apache Kafka
and the Confluent Platform.

%endif

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%if %{with python2}
%py2_build
%endif
%if %{with python3}
%py3_build
%endif

%install
%if %{with python2}
%py2_install
%endif
%if %{with python3}
%py3_install
# Fix ambiguous shebangs
pathfix.py -pni "%{__python3} %{py3_shbang_opts}" %{buildroot}%{python3_sitearch}/confluent_kafka
# Set executable bit for scripts that do not have it
chmod +x %{buildroot}%{python3_sitearch}/confluent_kafka/avro/cached_schema_registry_client.py
chmod +x %{buildroot}%{python3_sitearch}/confluent_kafka/avro/error.py
chmod +x %{buildroot}%{python3_sitearch}/confluent_kafka/avro/load.py
chmod +x %{buildroot}%{python3_sitearch}/confluent_kafka/avro/serializer/__init__.py
chmod +x %{buildroot}%{python3_sitearch}/confluent_kafka/avro/serializer/message_serializer.py
chmod +x %{buildroot}%{python3_sitearch}/confluent_kafka/kafkatest/verifiable_consumer.py
chmod +x %{buildroot}%{python3_sitearch}/confluent_kafka/kafkatest/verifiable_producer.py
%endif
# Remove license file installed in weird place
rm -f  %{buildroot}/%{_prefix}/LICENSE.txt

#%check
#%if %{with python2}
#py.test-2 -v --ignore=tests/integration ./tests/
#%endif
#%if %{with python3}
#py.test-3 -v --ignore=tests/integration ./tests/
#%endif

%if %{with python2}
%files -n python2-%{pypi_name}
%license LICENSE.txt
%doc README.md
%{python2_sitearch}/confluent_kafka
%{python2_sitearch}/confluent_kafka-%{version}-py?.?.egg-info
%endif

%if %{with python3}
%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.md
%{python3_sitearch}/confluent_kafka
%{python3_sitearch}/confluent_kafka-%{version}-py%{python3_version}.egg-info
%endif

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.11.6-9
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.11.6-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.11.6-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 24 2019 Javier Peña <jpena@redhat.com> - 0.11.16-3
- Fix python2-futures requirement
- Fix python2-enum34 for CentOS 7

* Fri Jan 11 2019 Javier Peña <jpena@redhat.com> - 0.11.16-2
- Fixed ambiguous shebangs
- Corrected description lines to avoid rpmlint errors

* Wed Dec 12 2018 Javier Peña <jpena@redhat.com> - 0.11.6-1
- Initial package.

%define name python-air
%define version 1.0
%define unmangled_version 1.0
%define unmangled_version 1.0
%define release 1

Summary: Python air module
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}_%{unmangled_version}.tar.gz
License: GPLv2+
Group: Development/Languages/Python
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArchitectures: noarch
BuildRequires: python
BuildRequires: python-setuptools

Requires: python >= 2.4
Requires: python-amqplib
Requires: python-json

Prefix: %{_prefix}
BuildArch: noarch
Vendor: David Greaves <david@dgreaves.com>
Url: http://github.com/lbt/ruote-amqp-pyclient

%description
Python air module

%prep
%setup -n %{name}-%{unmangled_version} -n %{name}-%{unmangled_version}

%build
python setup.py build

%install
python setup.py install --prefix=%{_prefix} --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
%dir /usr/lib/python?.?/site-packages/AIR


%changelog
* Fri Jul 30 2010 Islam Amer <islam.amer at nokia.com>
- packaged 1.0
